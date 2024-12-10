from email.charset import add_alias

from aiogram import types
from loader import dp
from keyboards.inline.tg_bot1 import tg_bott, opshi_iln
from keyboards.inline.funk_btn import fun_iln

@dp.callback_query_handler(text="telegram")
async def tg_bot(call:types.CallbackQuery):
    text="""📌 Telegram bot Telegram messenjerida ishlaydigan avtomatlashtirilgan dasturiy ta'minot bo'lib, u foydalanuvchilarga turli vazifalarni bajarishda yordam beradi. Botlar avtomatik javob berish, ma'lumot taqdim etish, interaktiv xizmatlar ko'rsatish va boshqa ko'plab vazifalarni amalga oshiradi.

🗣 Telegram botlar foydalanuvchi so'rovlariga javob berish, ma'lumotlarni qayta ishlash, API lar bilan integratsiya qilish va boshqa ko'plab funktsiyalarni bajarish uchun ishlab chiqilgan. Ular foydalanuvchi bilan muloqot qilish uchun matn, rasmlar, videolar, tugmalar va boshqa interaktiv elementlarni ishlatishi mumkin.

🐍 Python Telegram botlarini yaratishda keng qo'llaniladigan dasturlash tillaridan biridir. Python uchun mavjud bo'lgan kutubxonalar va ramkalar Telegram botlarini yaratishni osonlashtiradi. Ushbu kutubxonalarga pyTelegramBotAPI, python-telegram-bot va telepot kiradi. Ular botlarni yaratish, xabarlarni qayta ishlash, tugmalar va menyularni sozlash kabi vazifalarni osonlashtiradi.

🗂 Telegram botlari foydalanuvchilarga turli xizmatlarni taqdim etishi mumkin, jumladan, ob-havo ma'lumotlari, yangiliklar yangilanishlari, savdo jarayonlari, o'yinlar va ko'ngilochar xizmatlar, ma'lumotlar bazasidan ma'lumotlar olish va boshqalar.

🛠 Telegram bot ishlab chiquvchilari botning logikasini yaratish, foydalanuvchi interfeysi bilan ishlash, ma'lumotlar bazasi bilan integratsiya qilish va xavfsizlikni ta'minlash kabi vazifalar bilan shug'ullanadi. Shuningdek, ular botning ishlashini va foydalanuvchi tajribasini yaxshilash uchun muntazam ravishda optimallashtirish va yangilash ishlarini olib boradilar.

💰 Telegram botlari nafaqat foydalanuvchilarga qulaylik yaratadi, balki bizneslar uchun ham katta foyda keltiradi. Ular mijozlar bilan avtomatlashtirilgan muloqot o'rnatish, mijozlarga xizmat ko'rsatishni yaxshilash va xarajatlarni kamaytirishga yordam beradi. Python ning qulayligi va kuchli kutubxonalari Telegram botlarini yaratishda uni ideal tanlov qiladi."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=tg_bott)


@dp.callback_query_handler(text="ociqdar_tg")
async def ociq_fun(call:types.CallbackQuery):
    text="""📹 Telegram bot ochiq dars video tayorlanmoqda tez orada botga joylanadi..."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=opshi_iln)


@dp.callback_query_handler(text="kursdovomida_tg")
async def kurs_fun(call:types.CallbackQuery):
    img=open('static/imeges/img_2.png','rb')
    text=""""🤖 Kursing davomiyligi 2 oy bo’lib, haftada 3 kun 1, 1.5 soat dan bo’lib o’tadi. Kurs davomida siz:

— Telegram Bot ning boshlang'ich tushunchalari; 
— Bir nechta soda botlar yaratish;
— Default Keyboard va Inline keyboard bilan ishlash;
— Qo'shimcha funksiyalar bilan ishlash(Hujjatlar va media);
— Bot uchun shablon bilan tanishish;
— Handlers (Filterlar);
— Guruxlar bilan ishlovchi botlar;
— Kanallar bilan ishlovchi botlar;
— Ma`lumotlar ombori. SQLITE;
— BOT orqali to'lov;
— Botni serverga yuklash;
— GitHub bilan ishlashni o'rganish;


💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov:
   👤 Individual 1 200 000  so'm.
   👥 Gurux bilan  800 000 so'm"""
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text, reply_markup=opshi_iln)


@dp.callback_query_handler(text="botshablon_tg")
async def shablon_fun(call:types.CallbackQuery):
    ime=open('static/book/shablon (5).zip','rb')
    text="Telegram bot shabloni"
    await call.message.delete()
    await call.message.answer_document(document=ime,caption=text,reply_markup=opshi_iln)



@dp.callback_query_handler(text="backie")
async def backe_fun(call:types.CallbackQuery):
    text="""📌 Telegram bot Telegram messenjerida ishlaydigan avtomatlashtirilgan dasturiy ta'minot bo'lib, u foydalanuvchilarga turli vazifalarni bajarishda yordam beradi. Botlar avtomatik javob berish, ma'lumot taqdim etish, interaktiv xizmatlar ko'rsatish va boshqa ko'plab vazifalarni amalga oshiradi.

🗣 Telegram botlar foydalanuvchi so'rovlariga javob berish, ma'lumotlarni qayta ishlash, API lar bilan integratsiya qilish va boshqa ko'plab funktsiyalarni bajarish uchun ishlab chiqilgan. Ular foydalanuvchi bilan muloqot qilish uchun matn, rasmlar, videolar, tugmalar va boshqa interaktiv elementlarni ishlatishi mumkin.

🐍 Python Telegram botlarini yaratishda keng qo'llaniladigan dasturlash tillaridan biridir. Python uchun mavjud bo'lgan kutubxonalar va ramkalar Telegram botlarini yaratishni osonlashtiradi. Ushbu kutubxonalarga pyTelegramBotAPI, python-telegram-bot va telepot kiradi. Ular botlarni yaratish, xabarlarni qayta ishlash, tugmalar va menyularni sozlash kabi vazifalarni osonlashtiradi.

🗂 Telegram botlari foydalanuvchilarga turli xizmatlarni taqdim etishi mumkin, jumladan, ob-havo ma'lumotlari, yangiliklar yangilanishlari, savdo jarayonlari, o'yinlar va ko'ngilochar xizmatlar, ma'lumotlar bazasidan ma'lumotlar olish va boshqalar.

🛠 Telegram bot ishlab chiquvchilari botning logikasini yaratish, foydalanuvchi interfeysi bilan ishlash, ma'lumotlar bazasi bilan integratsiya qilish va xavfsizlikni ta'minlash kabi vazifalar bilan shug'ullanadi. Shuningdek, ular botning ishlashini va foydalanuvchi tajribasini yaxshilash uchun muntazam ravishda optimallashtirish va yangilash ishlarini olib boradilar.

💰 Telegram botlari nafaqat foydalanuvchilarga qulaylik yaratadi, balki bizneslar uchun ham katta foyda keltiradi. Ular mijozlar bilan avtomatlashtirilgan muloqot o'rnatish, mijozlarga xizmat ko'rsatishni yaxshilash va xarajatlarni kamaytirishga yordam beradi. Python ning qulayligi va kuchli kutubxonalari Telegram botlarini yaratishda uni ideal tanlov qiladi."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=tg_bott)


@dp.callback_query_handler(text="backee")
async def backe_fun(call:types.CallbackQuery):
    text="""📌 Python Foundation, Telegram Bot va Python Backend bo'yicha onlayn individual darslar

📚 Python Foundation bo'yicha darslar:
Python dasturlash tilini o'rganishni istaysizmi? Bizning individual onlayn darslarimiz orqali Python asoslarini mukammal o'zlashtirishingiz mumkin.

👨🏻‍💻 Telegram Bot yaratish bo'yicha darslar:
Telegram botlarini yaratishni o'rganmoqchimisiz? Bizning darslarimiz sizga Python yordamida kuchli va foydali Telegram botlarini yaratish bo'yicha bilim va ko'nikmalarni beradi.

🐍 Python Backend bo'yicha darslar:
Web-ilovalar va dasturiy tizimlarning orqa qismini yaratishni o'rganishni xohlaysizmi? Python backend dasturlarini ishlab chiqish bo'yicha individual darslarimiz sizga kerakli bilim va tajribani taqdim etadi."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=fun_iln)