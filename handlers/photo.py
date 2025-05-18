import os
import psycopg2
from aiogram import types, F
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.bot import dp, bot, model2, device, user_results
from utils.predict import predict_image
from utils.user_table import log_user_if_new
from config import ttoken
import logging

@dp.message(F.photo)
async def download_photo(message: types.Message):
    log_user_if_new(message.from_user)

    temp_dir = '/tmp' if os.name != 'nt' else './temp'
    os.makedirs(temp_dir, exist_ok=True)
    destination = os.path.join(temp_dir, f"{message.photo[-1].file_id}.jpg")

    await bot.download(message.photo[-1], destination=destination)
    logging.info(f"received photo from user {message.from_user.id}")
    if os.path.exists(destination):
        prediction = predict_image(destination, model2, device)
        try:
            connection = psycopg2.connect(
                host=ttoken.host,
                database=ttoken.db_name,
                user=ttoken.user,
                password=ttoken.password
            )
            with connection.cursor() as cursor:
                query = 'SELECT names, descs FROM data WHERE id IN %s;'
                cursor.execute(query, (prediction,))
                results = cursor.fetchall()
                user_results[message.from_user.id] = results

        except Exception as e:
            await message.answer("Ошибка при получении информации из БД.")
            logging.error("DB error: %s", e)
            return
        finally:
            if connection:
                connection.close()

        top_buttons = [types.InlineKeyboardButton(text=results[i][0], callback_data=f"top{i+1}") for i in range(3)]

        builder = InlineKeyboardBuilder()
        builder.row(*top_buttons)

        await message.answer(
            f'Вероятнее всего, это <b>{results[0][0].lower()}</b> или <b>{results[1][0].lower()}</b> или <b>{results[2][0].lower()}</b>',
            parse_mode=ParseMode.HTML,
            reply_markup=builder.as_markup()
        )
    else:
        await message.answer("Не удалось сохранить фото.")
    
    os.remove(destination)
