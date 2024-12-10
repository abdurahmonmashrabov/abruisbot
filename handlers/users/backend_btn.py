from aiogram import types
from loader import dp
from keyboards.inline.backend_iln import bekend_iln
from keyboards.inline.backend_iln import shablon_iln, ortga_iln
from keyboards.inline.funk_btn import fun_iln

@dp.callback_query_handler(text="py_backend")
async def backend_fun(call:types.CallbackQuery):
    text="""📌 Backend Python  dasturlash tili veb-ilovalar va boshqa dasturiy tizimlarning orqa qismini yaratish va boshqarish uchun ishlatiladigan dasturiy ta'minotni ishlab chiqishni anglatadi.

👨🏻‍💻 Python backend-bu mijoz tomoni (frontend) so'rovlarini ko'rib chiqadigan va ma'lumotlar bazalari bilan o'zaro aloqada bo'lgan, biznes mantig'ini bajaradigan, xavfsizlik, ma'lumotlarni qayta ishlash va boshqa funktsiyalarni ta'minlaydigan dasturlarning server tomoni.

🐍 Python backend dasturlarini ishlab chiqishni osonlashtiradigan ko'plab kutubxonalar va ramkalarni taklif etadi. Backend rivojlanishi uchun ba'zi mashhur Python ramkalariga Django, Flask, Pyramid va Bottle kiradi. Ular marshrutlarni boshqarish, ma'lumotlar bazalari bilan ishlash, API ishlab chiqish va backend ishlab chiqish uchun zarur bo'lgan boshqa vazifalar uchun qulay vositalarni taqdim etadi.

🗂 Python ma'lumotlar fani va ma'lumotlarni tahlil qilishda ham keng qo'llaniladi, bu esa uni katta hajmdagi ma'lumotlarni qayta ishlash va mashinani o'rganish bilan bog'liq tizimlarni backend ishlab chiqish uchun foydali qiladi.

🪩 Backend Python ishlab chiquvchilari server kodini yaratish va optimallashtirish, ma'lumotlar bazasini boshqarish, so'rovlarni qayta ishlash, biznes mantig'ini amalga oshirish va ilovaning xavfsizligi va ishlashini ta'minlash bilan shug'ullanadi.

📚 Backend Python Python tilining soddaligi va ekspressivligi, keng funktsionalligi va kutubxonalar va ramkalarning boy ekotizimi tufayli ko'plab ishlab chiquvchilar uchun mashhur tanlovdir."""
    await call.message.delete()
    await call.message.answer(text, reply_markup=bekend_iln)


@dp.callback_query_handler(text="ochiqd_dars_bac")
async def ochiqda_fun(call:types.CallbackQuery):
    text="""📽 Python Beckend ochiq dars video tayorlanmoqda tez orada botga joylanadi..."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=ortga_iln)


@dp.callback_query_handler(text="kurs_dovomida_bac")
async def kurs_dovomida_fun(call:types.CallbackQuery):
    imh=open('static/imeges/img_3.png','rb')
    text="""💻  Kursing davomiyligi 5 oy bo’lib, haftada 3 kun 2 soat dan bo’lib o’tadi. Kurs davomida siz:

— Internet infrastrukturasi protokollar haqida tushuncha;
— Sof SQL bilan ishlash va murakkab so'rovlarni optimallashtirish;
— Fayllarni server va databasega saqlash va olish;
— Django web framework arxitekturasi ishlash mexanizmi;
— MVT da sayt yoza olish
— API ishlab chiqish, uchinchi tomon xizmatlari bilan integratsiya;
— Dokumentatsiya yaratish va undan foydalansh;
— Web texlogiyalari va ularning ishlash mexanizmi;
— Rest full api yoza olish;
— Konteynerlash texnologiyalari, Deploy qilish;
— Python web frameworklari afzalliklari va kamchiliklar;
 
💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov:
   👤 Individual 1 500 000  so'm.
   👥 Gurux bilan 8 000 000 so'm"""
    await call.message.delete()
    await call.message.answer_photo(photo=imh,caption=text,reply_markup=ortga_iln)


@dp.callback_query_handler(text="mvtshablon")
async def mvt_fun(call:types.CallbackQuery):
    img=open('static/imeges/img_4.png','rb')
    text="""🗂 Web sayt shablonlari

1 - Resume sayt
2 - Blog sayt
3 - eCommerce sayt"""
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=shablon_iln)


@dp.callback_query_handler(text="bac")
async def baxc_fun(call:types.CallbackQuery):
    text="""📌 Backend Python  dasturlash tili veb-ilovalar va boshqa dasturiy tizimlarning orqa qismini yaratish va boshqarish uchun ishlatiladigan dasturiy ta'minotni ishlab chiqishni anglatadi.

👨🏻‍💻 Python backend-bu mijoz tomoni (frontend) so'rovlarini ko'rib chiqadigan va ma'lumotlar bazalari bilan o'zaro aloqada bo'lgan, biznes mantig'ini bajaradigan, xavfsizlik, ma'lumotlarni qayta ishlash va boshqa funktsiyalarni ta'minlaydigan dasturlarning server tomoni.

🐍 Python backend dasturlarini ishlab chiqishni osonlashtiradigan ko'plab kutubxonalar va ramkalarni taklif etadi. Backend rivojlanishi uchun ba'zi mashhur Python ramkalariga Django, Flask, Pyramid va Bottle kiradi. Ular marshrutlarni boshqarish, ma'lumotlar bazalari bilan ishlash, API ishlab chiqish va backend ishlab chiqish uchun zarur bo'lgan boshqa vazifalar uchun qulay vositalarni taqdim etadi.

🗂 Python ma'lumotlar fani va ma'lumotlarni tahlil qilishda ham keng qo'llaniladi, bu esa uni katta hajmdagi ma'lumotlarni qayta ishlash va mashinani o'rganish bilan bog'liq tizimlarni backend ishlab chiqish uchun foydali qiladi.

🪩 Backend Python ishlab chiquvchilari server kodini yaratish va optimallashtirish, ma'lumotlar bazasini boshqarish, so'rovlarni qayta ishlash, biznes mantig'ini amalga oshirish va ilovaning xavfsizligi va ishlashini ta'minlash bilan shug'ullanadi.

📚 Backend Python Python tilining soddaligi va ekspressivligi, keng funktsionalligi va kutubxonalar va ramkalarning boy ekotizimi tufayli ko'plab ishlab chiquvchilar uchun mashhur tanlovdir."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=bekend_iln)


@dp.callback_query_handler(text="back")
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