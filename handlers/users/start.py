from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.defult_btn import start_btn
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=start_btn)


