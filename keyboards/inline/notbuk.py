from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

funksiya_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish📲", url="https://t.me/abuxon_7")
        ],
        [
            InlineKeyboardButton(text="Back↩️", callback_data="bick")
        ]
    ]
)