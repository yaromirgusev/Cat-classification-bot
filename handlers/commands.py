import psycopg2
from aiogram import types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from core.bot import dp
from utils.user_table import log_user_if_new
from config import ttoken
import logging

@dp.message(F.text, Command("start"))
async def start_cmd(message: types.Message):
    log_user_if_new(message.from_user)
    await message.answer(
        "Привет! Я бот, который может распознать породу кота по фото! Просто отправь мне фото своего кота и я отгадаю его породу, а также могу вывести тебе небольшую сводку по основным особенностям этой породы/ Также ты можешь использовать команду /mycats для просмотра добавленных котов 😺",
        parse_mode=ParseMode.HTML
    )

@dp.message(F.text, Command("mycats"))
async def list_user_cats(message: types.Message):
    user_id = message.from_user.id
    try:
        connection = psycopg2.connect(
            host=ttoken.host,
            database=ttoken.db_name,
            user=ttoken.user,
            password=ttoken.password
        )
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT breed_name, breed_desc FROM user_cats WHERE user_id = %s;",
                (user_id,)
            )
            rows = cursor.fetchall()

        if rows:
            text = "😺 <b>Ваши коты:</b>\n\n"
            for name, desc in rows:
                text += f"<b>{name}</b>\n{desc}\n\n"
        else:
            text = "Вы ещё не добавили ни одной породы кота 😿"

        await message.answer(text, parse_mode=ParseMode.HTML)

    except Exception as e:
        logging.error(f"Error fetching user's cats: {e}")
        await message.answer("Ошибка при получении данных.")
    finally:
        if connection:
            connection.close()
