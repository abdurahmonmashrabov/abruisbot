from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

tg_bott=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ochiq dars📹",callback_data="ociqdar_tg")
        ],
        [
            InlineKeyboardButton(text="Kurs dovomida🧑🏻‍🏫",callback_data="kursdovomida_tg"),
            InlineKeyboardButton(text="Bot shablon🗂",callback_data="botshablon_tg")
        ],
        [
            InlineKeyboardButton(text="Back↩️",callback_data="backee")
        ]
    ]
)
opshi_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish📲",url="https://t.me/abuxon_7")
        ],
        [
            InlineKeyboardButton(text="Back🔙",callback_data="backie")
        ]
    ]
)