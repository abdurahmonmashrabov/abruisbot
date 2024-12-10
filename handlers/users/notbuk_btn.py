from  aiogram import types
from loader import dp
from keyboards.inline.notbuk import funksiya_iln
from keyboards.inline.funk_btn import fun_iln

@dp.callback_query_handler(text="noutbuk")
async def notbuk_fun(call:types.CallbackQuery):
    text="""👨🏻‍💻 Dasturlash uchun talab qilinadigan minimum noutbuk, agar yangi olmoqchi bo’lsangiz:

🔸 Kami bilan Core i5 (10-avlod) yoki AMD Ryzen 5 (Core i7 bo’lsa yaxshi)
🔸 Tezkor xotira RAM kami bilan 8GB (16 bo'lsa yaxshi)\- Asosiy Xotira SSD kami bilan 256 GB

💻 Agar Apple MacBook olmoqchi bo’lsangiz va pulingiz yetarli bo’lsa:

🔹 Kami bilan M1 Protsessor
🔹 Kami bilan 8GB RAM xotira
🔹 Kami bilan 256GB doimiy SSD xotira

🖥 Agar oldingi kompyuteringiz bo’lsa uning texnik holatini quyidagilarga keltirib olishingiz maqsadga muvofiq:

🔻 RAM xotira 8GB kamida;
🔻 Agar HDD xotira bo’lsa, uni kamida 256GB SSDga almashtirish yoki HDD yoniga o’rnatish"""
    await call.message.delete()
    await call.message.answer(text,reply_markup=funksiya_iln)


@dp.callback_query_handler(text="bick")
async def bick_fun(call:types.CallbackQuery):
    text="""📌 Python Foundation, Telegram Bot va Python Backend bo'yicha onlayn individual darslar

📚 Python Foundation bo'yicha darslar:
Python dasturlash tilini o'rganishni istaysizmi? Bizning individual onlayn darslarimiz orqali Python asoslarini mukammal o'zlashtirishingiz mumkin.

👨🏻‍💻 Telegram Bot yaratish bo'yicha darslar:
Telegram botlarini yaratishni o'rganmoqchimisiz? Bizning darslarimiz sizga Python yordamida kuchli va foydali Telegram botlarini yaratish bo'yicha bilim va ko'nikmalarni beradi.

🐍 Python Backend bo'yicha darslar:
Web-ilovalar va dasturiy tizimlarning orqa qismini yaratishni o'rganishni xohlaysizmi? Python backend dasturlarini ishlab chiqish bo'yicha individual darslarimiz sizga kerakli bilim va tajribani taqdim etadi."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=fun_iln)