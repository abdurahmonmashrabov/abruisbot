from aiogram import types
from loader import dp
from keyboards.inline.admin_iln import rustam_iln,ijtimoiy_iln,ortga_iln


@dp.callback_query_handler(text="resume")
async def resume_fun(call:types.CallbackQuery):
    img=open('static/book/resume (8).pdf','rb')
    await call.message.delete()
    await call.message.answer_document(document=img,reply_markup=ortga_iln)



@dp.message_handler(text="👨🏻‍💻 Isroilov Rustam")
async def rustam(message:types.Message):
    img=open('static/imeges/img_5.png','rb')
    text="""👨‍🏫 Mentor: Isroilov Rustamjon
🧑‍💻 Kasbi: Python Foundation va Beckend mentor (3-yilik tajriba, 250+ shogirtlar)
⚙️ Texnik ko'nikmalari: Python, Telegram Bot, Django, Django Rest, SQLite, PostgreSQL, Git, GitHub, HTML, CSS, C++, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)
💼 Ish joyti: Isystem IT Academy (2022-hozirgacha)
📍 Yashash manzili: Toshkent shahar"""
    await message.delete()
    await message.answer_photo(photo=img,caption=text,reply_markup=rustam_iln)


@dp.callback_query_handler(text="ijtimoyi")
async def tarmoq_fun(call:types.CallbackQuery):
    img=open("static/imeges/img_6.png",'rb')
    await call.message.delete()
    await call.message.answer_photo(photo=img,reply_markup=ijtimoiy_iln)


@dp.callback_query_handler(text="backe")
async def bace_fun(call:types.CallbackQuery):
    img=open('static/imeges/img_5.png','rb')
    text="""👨‍🏫 Mentor: Isroilov Rustamjon
🧑‍💻 Kasbi: Python Foundation va Beckend mentor (3-yilik tajriba, 250+ shogirtlar)
⚙️ Texnik ko'nikmalari: Python, Telegram Bot, Django, Django Rest, SQLite, PostgreSQL, Git, GitHub, HTML, CSS, C++, Microsoft Office(Word, Excel, Power Point, Paint, va h.k.lar)
💼 Ish joyti: Isystem IT Academy (2022-hozirgacha)
📍 Yashash manzili: Toshkent shahar"""
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=rustam_iln)

@dp.callback_query_handler(text="karzinka")
async def karzinka_fun(call:types.CallbackQuery):
    await call.message.delete()