from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

rustam_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Resume",callback_data="resume")
        ],
        [
            InlineKeyboardButton(text="Ijtimoiy tarmoqlar",callback_data="ijtimoyi")
        ],
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish",url="https://t.me/abuxon_7")
        ],
        [
            InlineKeyboardButton(text="🗑",callback_data="karzinka")
        ]
    ]
)
ijtimoiy_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Linkedin",url="https://www.linkedin.com/"),
            InlineKeyboardMarkup(text="GitHub",url="https://github.com/")
        ],
        [
            InlineKeyboardButton(text="Instagram",url="https://www.instagram.com/"),
            InlineKeyboardMarkup(text="YouTube",url="https://www.youtube.com/")
        ],
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish",urt="https://t.me/abuxon_7")
        ],
        [
            InlineKeyboardButton(text="Back",callback_data="backe")
        ]
    ]
)
ortga_iln=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram orqali bog'lanish", url="https://t.me/abuxon_7")
        ],
        [
            InlineKeyboardButton(text="Back", callback_data="backe")
        ]
    ]
)

