from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

start_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📑 Kurs haqidim ma'lumotlar(Online)")
        ],
        [
            KeyboardButton(text="👨🏻‍💻 Isroilov Rustam"),
            KeyboardButton(text="📰Web Site")
        ],
        [
            KeyboardButton(text="🧾 Kurska ro'yhatan o'tish")
        ]
    ],
    resize_keyboard=True
)