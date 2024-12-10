from aiogram import types
from aiogram.utils.exceptions import BadWebhook

from loader import dp
from keyboards.inline.funk_btn import fun_iln,foun_fun,orqaga_iln,misolar_iln

@dp.message_handler(text="📑 Kurs haqidim ma'lumotlar(Online)")
async def kurs_fun(message:types.Message):
    img=open("static/imeges/img.png","rb")
    text="""📌 Python Foundation, Telegram Bot va Python Backend bo'yicha onlayn individual darslar

📚 Python Foundation bo'yicha darslar:
Python dasturlash tilini o'rganishni istaysizmi? Bizning individual onlayn darslarimiz orqali Python asoslarini mukammal o'zlashtirishingiz mumkin.

👨🏻‍💻 Telegram Bot yaratish bo'yicha darslar:
Telegram botlarini yaratishni o'rganmoqchimisiz? Bizning darslarimiz sizga Python yordamida kuchli va foydali Telegram botlarini yaratish bo'yicha bilim va ko'nikmalarni beradi.

🐍 Python Backend bo'yicha darslar:
Web-ilovalar va dasturiy tizimlarning orqa qismini yaratishni o'rganishni xohlaysizmi? Python backend dasturlarini ishlab chiqish bo'yicha individual darslarimiz sizga kerakli bilim va tajribani taqdim etadi."""
    await message.delete()
    await message.answer_photo(photo=img,caption=text,reply_markup=fun_iln)


@dp.callback_query_handler(text="foundatiion")
async def fan_fin(call:types.CallbackQuery):
    text="""📌 Dasturlash asoslarini o'rganish bir nechta muhim sabablarga ega:

📚 Dasturlash mantig'ini tushunish: dasturlash asoslari dasturlarning mantig'i va ishlash tamoyillarini tushunishga imkon beradi. Siz kompyuterlar ma'lumotni qanday qayta ishlashini va ma'lumotlar bilan qanday munosabatda bo'lishini bilib olasiz.

🔍 Algoritmik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish algoritmik fikrlash ko'nikmalarini va murakkab vazifalarni sodda va tushunarli bosqichlarga bo'lish qobiliyatini rivojlantirishga yordam beradi. Siz samarali muammolarni hal qilish algoritmlarini ishlab chiqishingiz mumkin.

👥  Jamoa bilan ishlash: dasturlash asoslarini bilish sizga boshqa ishlab chiquvchilar bilan samarali hamkorlik qilish imkonini beradi. Siz umumiy tilda tushunishingiz va muloqot qilishingiz, boshqa ishlab chiquvchilar tomonidan yaratilgan kodni osonroq ajratishingiz va tushunishingiz mumkin.

🚀 Analitik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish analitik fikrlash va muammolarni muntazam ravishda hal qilish qobiliyatini rivojlantiradi. Siz muammolarni tahlil qilishni, ularning sabablarini topishni va oqilona echimlarni ishlab chiqishni o'rganasiz.

🦾 Texnologiyaning texnik tomonini tushunish: texnologiyaga boy dunyoda dasturlash asoslarini tushunish sizga texnik echimlar va texnologik mahsulotlar bilan yaxshiroq tushunish va o'zaro aloqada bo'lishga yordam beradi.

🎓 Dasturlash asoslarini o'rganish sizga nafaqat o'ziga xos dasturlash ko'nikmalarini beradi, balki tanqidiy fikrlash, ijodkorlik va muammoli fikrlashni rivojlantirishga yordam beradi. Ushbu ko'nikmalar nafaqat dasturlash sohasida, balki faoliyatning turli sohalarida ham qimmatli va foydalidir."""
    await call.message.delete()
    await call.message.answer(text, reply_markup=foun_fun)


@dp.callback_query_handler(text="ociqdars_fon")
async def ocq_fun(call:types.CallbackQuery):
    text="""🎥 Foundation ochiq dars video tayorlanmoqda tez orada botga joylanadi..."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=orqaga_iln)


@dp.callback_query_handler(text="kurs_dovomida_fon")
async def kurs_fun(call:types.CallbackQuery):
    imge=open('static/imeges/img_1.png','rb')
    text="""💻  Kursing davomiyligi 3 oy bo’lib, haftada 3 kun 1, 1.5 soat dan bo’lib o’tadi. Kurs davomida siz:

— Python dasturlash tilining boshlang'ich tushunchalari; 
— Python da ma’lumot turlari, o’zgaruvchilar bilan ishlash;
— Axborot texnologiyalari. Kompyuterning texnik va dasturiy ta’minoti;
— Algoritm tushunchasi va turlari;
— Tartiblash algoritmlar;
— Ma'lumotlar strukturasini;
— Funksiya, satr va massivlar bilan ishlashni
— Obyektga yo'naltirilgan dasturlashni(OOP) o'rganasiz. 
— LeetCode  


💸 Kurslarning narxiga keladigan bo'lsak

🔰 Oldindan oyiga to’lov:
   👤 Individual 1 000 000  so'm.
   👥 Gurux bilan 500 000 so'm"""
    await call.message.delete()
    await call.message.answer_photo(photo=imge,caption=text,reply_markup=orqaga_iln)


@dp.callback_query_handler(text="ornatish")
async def ornatish_fun(call:types.CallbackQuery):
    text="""📥 Pythonni o'rnatish haqida video tayorlanmoqda tez orada botga joylanadi..."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=orqaga_iln)


@dp.callback_query_handler(text="misollar")
async def misol_fun(call:types.CallbackQuery):
    img=open('static/imeges/img_2.png','rb')
    text="""📝 Foundation misolar to’plami
    
1 - Print funksiyasiga doir misolar
2 - O'zgaruvchilar, Data Types, Input()
3 - Shart operatorlar
4 - While sikl operatori
5 - For sikl operatori
6 - Ro’yxatlar (List)
7 - Tuple, Set
8 - Dictionary misolar
9 - Funksiya (def)
10 - Rekursiv funksiya va *args, **kwargs
11 - 2D arrays
12 - LeetCode"""
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=misolar_iln)


@dp.callback_query_handler(text="karzinka")
async def karzinka(call:types.CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(text="biick")
async def biick_fun(call:types.CallbackQuery):
    text="""📌 Dasturlash asoslarini o'rganish bir nechta muhim sabablarga ega:

    📚 Dasturlash mantig'ini tushunish: dasturlash asoslari dasturlarning mantig'i va ishlash tamoyillarini tushunishga imkon beradi. Siz kompyuterlar ma'lumotni qanday qayta ishlashini va ma'lumotlar bilan qanday munosabatda bo'lishini bilib olasiz.

    🔍 Algoritmik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish algoritmik fikrlash ko'nikmalarini va murakkab vazifalarni sodda va tushunarli bosqichlarga bo'lish qobiliyatini rivojlantirishga yordam beradi. Siz samarali muammolarni hal qilish algoritmlarini ishlab chiqishingiz mumkin.

    👥  Jamoa bilan ishlash: dasturlash asoslarini bilish sizga boshqa ishlab chiquvchilar bilan samarali hamkorlik qilish imkonini beradi. Siz umumiy tilda tushunishingiz va muloqot qilishingiz, boshqa ishlab chiquvchilar tomonidan yaratilgan kodni osonroq ajratishingiz va tushunishingiz mumkin.

    🚀 Analitik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish analitik fikrlash va muammolarni muntazam ravishda hal qilish qobiliyatini rivojlantiradi. Siz muammolarni tahlil qilishni, ularning sabablarini topishni va oqilona echimlarni ishlab chiqishni o'rganasiz.

    🦾 Texnologiyaning texnik tomonini tushunish: texnologiyaga boy dunyoda dasturlash asoslarini tushunish sizga texnik echimlar va texnologik mahsulotlar bilan yaxshiroq tushunish va o'zaro aloqada bo'lishga yordam beradi.

    🎓 Dasturlash asoslarini o'rganish sizga nafaqat o'ziga xos dasturlash ko'nikmalarini beradi, balki tanqidiy fikrlash, ijodkorlik va muammoli fikrlashni rivojlantirishga yordam beradi. Ushbu ko'nikmalar nafaqat dasturlash sohasida, balki faoliyatning turli sohalarida ham qimmatli va foydalidir."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=foun_fun)