import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

bot = Bot(token="8718270593:AAG_vB27iyMAeGto4EHJViDbxaY27Gbrm")
dp = Dispatcher()
# ------------------- МЕНЮ 1: KURS -------------------
kurs_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1-kurs")],
        [KeyboardButton(text="2-kurs")]
    ],
    resize_keyboard=True
)

# =================== 1-KURS TARAWLAR ===================
kurs1_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Jeke tártiptegi kiyim tıgıwshısı")],
        [KeyboardButton(text="Shashtarez (modelleri)")],
        [KeyboardButton(text="Elektrik")],
        [KeyboardButton(text="Baylanıs Operatori")],
        [KeyboardButton(text="Xabar qurallari mashinaları hám kompyuter tarmaqları operatori")],
        [KeyboardButton(text="Avtomobillerdi onlaw hám olarga texnik xizmet kòrsetiw")],
        [KeyboardButton(text="⬅️ Artqa (bas menu)")]
    ],
    resize_keyboard=True
)

# =================== TIGIWSHILIK MENU ===================
tigiwshisi_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Tigiwshilik mashinaların sazlaw jumısları (o'a)")],
        [KeyboardButton(text="Tigiwshilik mashinaların sazlaw")],
        [KeyboardButton(text="Keń Assortimenttegi kiyimlerdi tigiw (o'a)")],
        [KeyboardButton(text="Keń Assortimenttegi kiyimlerdi tigiw texnologyasi")],
        [KeyboardButton(text="Keń Assortimenttegi kiyimlerdi konstruksiyalaw hám modellestiriw")],
        [KeyboardButton(text="Tigiwshilik tiykarları")],
        [KeyboardButton(text="Miynetti qogaw ham qawipsizlik texnikasi")],
        [KeyboardButton(text="Tigiwshilik material taniw")],
        [KeyboardButton(text="JSHSHBT")],
        [KeyboardButton(text="Dene tarbiya")],
        [KeyboardButton(text="Ximya")],
        [KeyboardButton(text="Fizika hám astranomiya")],
        [KeyboardButton(text="Informatika hám informaciya texnologiyaları")],
        [KeyboardButton(text="Matematika")],
        [KeyboardButton(text="Tarbiya")],
        [KeyboardButton(text="Tarix")],
        [KeyboardButton(text="Ingliz tili")],
        [KeyboardButton(text="Ózbek tili")],
        [KeyboardButton(text="Rus tili")],
        [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
        [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
    ],
    resize_keyboard=True
)

# =================== AVTO MENU ===================
avto_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Avtomobil dvigatellerine servis xizmet kórsetiw hám remontlaw jumıslar (óa)")],
        [KeyboardButton(text="Janılǵini támiyinlew sistemasına servis xizmet kórsetiw hám remontlaw jumısları")],
        [KeyboardButton(text="Avtomobil dvigatellerine servis xizmet kórsetiw hám remontlaw")],
        [KeyboardButton(text="Avtomobil elektr hám elektron úskeneleri")],
        [KeyboardButton(text="Temirshi ustalıq jumısı (óa)")],
        [KeyboardButton(text="Avtomobil duzulishi")],
        [KeyboardButton(text="Miynet qáwipsizligi hám qawipsizlik texnikasi")],
        [KeyboardButton(text="Texnikalıq Sızıwshılıq")],
        [KeyboardButton(text="JSHSHT")],
        [KeyboardButton(text="Denetarbiya")],
        [KeyboardButton(text="Fizika hám astranomiya")],
        [KeyboardButton(text="Informatika hám informaciya texnologiyaları")],
        [KeyboardButton(text="Matematika")],
        [KeyboardButton(text="Tarbiya")],
        [KeyboardButton(text="Tarix")],
        [KeyboardButton(text="Ingliz tili")],
        [KeyboardButton(text="Ózbek tili")],
        [KeyboardButton(text="Rus tili")],
        [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
        [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
    ],
    resize_keyboard=True
)


# =================== XABAR MENU ===================
xabar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kompyuter arxitekturası hám ofis úskenelerine texnikalıq xizmet kórsetiw (óa)")],
        [KeyboardButton(text="Kompyuter arxitekturası hám ofis úskenelerine texnikalıq xizmet kórsetiw")],
        [KeyboardButton(text="Web programmalaw hám dizayn")],
        [KeyboardButton(text="Kompyuter sistemalarınıń programmalıq támiynatı")],
        [KeyboardButton(text="Kompyuter tarmaqları hám administratorlaw")],
        [KeyboardButton(text="Programmalastırıw tiykarları")],
        [KeyboardButton(text="Informaciya qawipsizligi")],
        [KeyboardButton(text="Media hám informaciya sawatlılıq")],
        [KeyboardButton(text="Miynetti qorgaw hám qawipsizlik texnikasi")],
        [KeyboardButton(text="JSHSHBT")],
        [KeyboardButton(text="Denetarbiya")],
        [KeyboardButton(text="Fizika hám astranomiya")],
        [KeyboardButton(text="Informatika hám informaciya texnologiyaları")],
        [KeyboardButton(text="Matematika")],
        [KeyboardButton(text="Tarbiya")],
        [KeyboardButton(text="Tarix")],
        [KeyboardButton(text="Ingliz tili")],
        [KeyboardButton(text="Ózbek tili (qaraqalpaq klass)")],
        [KeyboardButton(text="Rus tili (qoraqalpoq sinf)")],
        [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
        [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
    ],
    resize_keyboard=True
)

# =================== BAYLANIS MENU ===================
baylanis_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Optikalıq talshıqlı hám elektr baylanıs kabellerge texnikalıq xizmet kórsetiw hám remontlaw (o’a)")],
        [KeyboardButton(text="Qalalarara hám xalıq aralıq baylanıs tarmaqları")],
        [KeyboardButton(text="Optikalıq talshıqlı hám elektr baylanıs kabelleri")],
        [KeyboardButton(text="Miynet qáwipsizligi hám qawipsizlik texnikası")],
        [KeyboardButton(text="Baylanıs qurılmaların elektr támiynatı")],
        [KeyboardButton(text="Baylanıs ólshew texnikası")],
        [KeyboardButton(text="Elektronika hám elektrotexnika tiykarları")],
        [KeyboardButton(text="JSHSHT")],
        [KeyboardButton(text="Denetarbiya")],
        [KeyboardButton(text="Fizika hám astranomiya")],
        [KeyboardButton(text="Informatika hám informaciya texnologiyaları")],
        [KeyboardButton(text="Matematika")],
        [KeyboardButton(text="Tarbiya")],
        [KeyboardButton(text="Tarix")],
        [KeyboardButton(text="Ingliz tili")],
        [KeyboardButton(text="Ózbek tili (qaraqalpaq klass)")],
        [KeyboardButton(text="Rus tili (qoraqalpoq sinf)")],
        [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
        [KeyboardButton(text="Abonent kirisiw tarmaqları (o’a)")],
        [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
    ],
    resize_keyboard=True
)

# =================== ELEKTRIK MENU ===================
elektrik_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sanaat kárxanalardıń elektr úskenelerine xizmet kórsetiw hám sazlaw")],
        [KeyboardButton(text="Sanaat kárxanalardıń elektr úskenelerine xizmet kórsetiw hám sazlaw jumısları (óa)")],
        [KeyboardButton(text="Temirshi ustalıq jumısı (óa)")],
        [KeyboardButton(text="Xojalıq texnika elektr úskenelerdi sazlaw, remontlaw hám isletiw")],
        [KeyboardButton(text="Avtomatıka tiykarları hám mikroprocessor texnikasi")],
        [KeyboardButton(text="Miynet qáwipsizligi hám qawipsizlik texnikasi")],
        [KeyboardButton(text="Elektrotexnika materiallari")],
        [KeyboardButton(text="Texnikalıq Sızıwshılıq")],
        [KeyboardButton(text="Shaqırıwǵa shekem baslanǵısh tayarlıq")],
        [KeyboardButton(text="Dene tarbiyasi")],
        [KeyboardButton(text="Ximya")],
        [KeyboardButton(text="Fizika hám astranomiya")],
        [KeyboardButton(text="Informatika hám informaciya texnologiyalari")],
        [KeyboardButton(text="Matematika")],
        [KeyboardButton(text="Tarbiya")],
        [KeyboardButton(text="Tarix")],
        [KeyboardButton(text="Ingliz tili")],
        [KeyboardButton(text="Ózbek tili")],
        [KeyboardButton(text="Rus tili")],
        [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
        [KeyboardButton(text="Elektronika hám elektrotexnika tiykarlari")],
        [KeyboardButton(text="Sanaat kárxanaları hám puqaralıq imaratlarınıń elektr úskeneleri")],
        [KeyboardButton(text="Xojalıq texnika elektr úskenelerdi sazlaw hám remontlaw jumısları (óa)")],
        [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
    ],
    resize_keyboard=True
)

# =================== SHASHTAREZ MENU ===================
shashtarez_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kórkem pardozlaw jumısları")],
        [KeyboardButton(text="Kórkem shash turmeklew hám modellestiriw")],
        [KeyboardButton(text="Shashtárezlik jumısları texnologiyası (óa)")],
        [KeyboardButton(text="Erler hám áyeller shashtárezi")],
        [KeyboardButton(text="Shashtárezlik jumısları materialları hám ásbap-úskeneleri")],
        [KeyboardButton(text="Miynetti qorǵaw hám qawipsizlik texnikasi")],
        [KeyboardButton(text="Shashtárezlik tiykarları")],
        [KeyboardButton(text="JSHSHBT")],
        [KeyboardButton(text="Dene tarbiya")],
        [KeyboardButton(text="Biologiya")],
        [KeyboardButton(text="Ximiya")],
        [KeyboardButton(text="Informatika hám informaciya texnologiyalari")],
        [KeyboardButton(text="Matematika")],
        [KeyboardButton(text="Tarbiya")],
        [KeyboardButton(text="Tarix")],
        [KeyboardButton(text="Ingliz tili")],
        [KeyboardButton(text="Ózbek tili")],
        [KeyboardButton(text="Rus tili")],
        [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
        [KeyboardButton(text="Kórkem shash túrmeklew hám modellestiriw texnologiyası (óa)")],
        [KeyboardButton(text="Ren suwret")],
        [KeyboardButton(text="Kásip etikası hám psixologiyası")],
        [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
    ],
    resize_keyboard=True
)

# =================== HANDLERS ===================
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("📚 Kursti tańlań:", reply_markup=kurs_menu)

@dp.message(F.text == "1-kurs")
async def kurs1(message: Message):
    await message.answer("📘 1-kurs tarawin tańlań:", reply_markup=kurs1_menu)

@dp.message(F.text == "⬅️ Artqa (bas menu)")
async def back_start(message: Message):
    await start(message)

@dp.message(F.text == "Jeke tártiptegi kiyim tıgıwshısı")
async def tigiw(message: Message):
    await message.answer("📘 Panlerdı tańlań:", reply_markup=tigiwshisi_menu)

@dp.message(F.text == "Avtomobillerdi onlaw hám olarga texnik xizmet kòrsetiw")
async def avto(message: Message):
    await message.answer("📘 Panlerdı tańlań:", reply_markup=avto_menu)

    # =================== ELEKTRIK MENU ===================
    elektrik_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Sanaat kárxanalardıń elektr úskenelerine xizmet kórsetiw hám sazlaw")],
            [KeyboardButton(text="Sanaat kárxanalardıń elektr úskenelerine xizmet kórsetiw hám sazlaw jumısları (óa)")],
            [KeyboardButton(text="Temirshi ustalıq jumısı (óa)")],
            [KeyboardButton(text="Xojalıq texnika elektr úskenelerdi sazlaw, remontlaw hám isletiw")],
            [KeyboardButton(text="Avtomatıka tiykarları hám mikroprocessor texnikasi")],
            [KeyboardButton(text="Miynet qáwipsizligi hám qawipsizlik texnikasi")],
            [KeyboardButton(text="Elektrotexnika materiallari")],
            [KeyboardButton(text="Texnikalıq Sızıwshılıq")],
            [KeyboardButton(text="Shaqırıwǵa shekem baslanǵısh tayarlıq")],
            [KeyboardButton(text="Dene tarbiyasi")],
            [KeyboardButton(text="Ximya")],
            [KeyboardButton(text="Fizika hám astranomiya")],
            [KeyboardButton(text="Informatika hám informaciya texnologiyalari")],
            [KeyboardButton(text="Matematika")],
            [KeyboardButton(text="Tarbiya")],
            [KeyboardButton(text="Tarix")],
            [KeyboardButton(text="Ingliz tili")],
            [KeyboardButton(text="Ózbek tili")],
            [KeyboardButton(text="Rus tili")],
            [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
            [KeyboardButton(text="Elektronika hám elektrotexnika tiykarlari")],
            [KeyboardButton(text="Sanaat kárxanaları hám puqaralıq imaratlarınıń elektr úskeneleri")],
            [KeyboardButton(text="Xojalıq texnika elektr úskenelerdi sazlaw hám remontlaw jumısları (óa)")],
            [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
        ],
        resize_keyboard=True
    )

    # =================== SHASHTAREZ MENU ===================
    shashtarez_menu = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Kórkem pardozlaw jumısları")],
            [KeyboardButton(text="Kórkem shash turmeklew hám modellestiriw")],
            [KeyboardButton(text="Shashtárezlik jumısları texnologiyası (óa)")],
            [KeyboardButton(text="Erler hám áyeller shashtárezi")],
            [KeyboardButton(text="Shashtárezlik jumısları materialları hám ásbap-úskeneleri")],
            [KeyboardButton(text="Miynetti qorǵaw hám qawipsizlik texnikasi")],
            [KeyboardButton(text="Shashtárezlik tiykarları")],
            [KeyboardButton(text="JSHSHBT")],
            [KeyboardButton(text="Dene tarbiya")],
            [KeyboardButton(text="Biologiya")],
            [KeyboardButton(text="Ximiya")],
            [KeyboardButton(text="Informatika hám informaciya texnologiyalari")],
            [KeyboardButton(text="Matematika")],
            [KeyboardButton(text="Tarbiya")],
            [KeyboardButton(text="Tarix")],
            [KeyboardButton(text="Ingliz tili")],
            [KeyboardButton(text="Ózbek tili")],
            [KeyboardButton(text="Rus tili")],
            [KeyboardButton(text="Qaraqalpaq tili hám ádebiyatı")],
            [KeyboardButton(text="Kórkem shash túrmeklew hám modellestiriw texnologiyası (óa)")],
            [KeyboardButton(text="Ren suwret")],
            [KeyboardButton(text="Kásip etikası hám psixologiyası")],
            [KeyboardButton(text="⬅️ Artqa (1-kurs)")]
        ],
        resize_keyboard=True
    )

    # =================== HANDLERS ===================
    @dp.message(CommandStart())
    async def start(message: Message):
        await message.answer("📚 Kursti tańlań:", reply_markup=kurs_menu)

    @dp.message(F.text == "1-kurs")
    async def kurs1(message: Message):
        await message.answer("📘 1-kurs tarawin tańlań:", reply_markup=kurs1_menu)

    @dp.message(F.text == "⬅️ Artqa (bas menu)")
    async def back_start(message: Message):
        await start(message)

    @dp.message(F.text == "Jeke tártiptegi kiyim tıgıwshısı")
    async def tigiw(message: Message):
        await message.answer("📘 Panlerdı tańlań:", reply_markup=tigiwshisi_menu)

    @dp.message(F.text == "Avtomobillerdi onlaw hám olarga texnik xizmet kòrsetiw")
    async def avto(message: Message):
        await message.answer("📘 Panlerdı tańlań:", reply_markup=avto_menu)
@dp.message(F.text == "Xabar qurallari mashinaları hám kompyuter tarmaqları operatori")
async def xabar(message: Message):
    await message.answer("📘 Panlerdı tańlań:", reply_markup=xabar_menu)

@dp.message(F.text == "Baylanıs Operatori")
async def baylanis(message: Message):
    await message.answer("📘 Panlerdı tańlań:", reply_markup=baylanis_menu)

@dp.message(F.text == "Elektrik")
async def elektrik(message: Message):
    await message.answer("📘 Panlerdı tańlań:", reply_markup=elektrik_menu)

@dp.message(F.text == "Shashtarez (modelleri)")
async def shashtarez(message: Message):
    await message.answer("📘 Panlerdı tańlań:", reply_markup=shashtarez_menu)

@dp.message(F.text == "⬅️ Artqa (1-kurs)")
async def back_kurs1(message: Message):
    await kurs1(message)

# =================== RUN ===================
async def main():
    await dp.start_polling(bot)

if __name__ == "main":
    asyncio.run(main())