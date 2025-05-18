from aiogram import types, F
from core.bot import dp, user_results
from utils.user_table import save_user_breed, log_user_if_new
import logging

@dp.callback_query(F.data.in_({"top1", "top2", "top3"}))
async def handle_top_choice(callback: types.CallbackQuery):
    user = callback.from_user
    log_user_if_new(user)

    results = user_results.get(user.id)
    if not results:
        await callback.message.answer("Нет данных для ответа. Попробуйте отправить фото ещё раз.")
        return

    index_map = {"top1": 0, "top2": 1, "top3": 2}
    idx = index_map.get(callback.data)
    breed_name, breed_desc = results[idx]

    save_user_breed(user.id, breed_name, breed_desc)

    logging.info(f"user {callback.from_user.id} selected {breed_name}")
    await callback.message.answer(breed_desc)
    await callback.answer()
