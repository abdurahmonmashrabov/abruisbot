from aiogram.types import  InlineKeyboardButton,InlineKeyboardMarkup

bekend_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ochiq dars📹",callback_data="ochiqd_dars_bac")
        ],
        [
            InlineKeyboardButton(text="Kurs davomida🧑🏻‍🏫",callback_data="kurs_dovomida_bac"),
            InlineKeyboardButton(text="MVT Shablon🗂", callback_data="mvtshablon")
        ],
        [
            InlineKeyboardButton(text="Back↩️",callback_data="back")
        ]
    ]
)
shablon_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1",callback_data="1"),
            InlineKeyboardButton(text="2",callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3")
        ],
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish📲",url="https://t.me/abuxon_7")
        ],
        [
            InlineKeyboardButton(text="Back🔙",callback_data="backe")
        ]
    ]
)
ortga_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish📲",url="https://t.me/abuxon_7")
        ],
        [
            InlineKeyboardButton(text="Back🔙", callback_data="bac")
        ]
    ]
)