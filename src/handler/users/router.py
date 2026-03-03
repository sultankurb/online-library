from aiogram import Router, types, F
from aiogram.filters import Command

from src.keyboards import create_keyboards
from .depends import get_all_courses_category


router = Router()
keybinds = create_keyboards(
"Jeke tártiptegi kiyim tıgıwshısı",
     "Shashtarez (modelleri)",
     "Elektrik",
     "Baylanıs Operatori",
     "Xabar qurallari mashinaları hám kompyuter tarmaqları operatori",
     "Avtomobillerdi onlaw hám olarga texnik xizmet kòrsetiw",
     "Menu"
)

kurs_keybinds = create_keyboards("1-kurs", "2-kurs",)

@router.message(Command(commands="start", prefix="/"))
async def start_command(message: types.Message):
    await message.answer(text="Ассалаума алейкум", reply_markup=kurs_keybinds)


@router.message(F.text == "1-kurs")
async def first_course(message: types.Message):
    answers = await get_all_courses_category(course_degree=1)
    await message.answer(
        text="Select",
        reply_markup=create_keyboards(*answers),
    )


@router.message(F.text == "2-kurs")
async def second_course(message: types.Message):
    answers = await get_all_courses_category(course_degree=2)
    await message.answer(
        text="Select",
        reply_markup=create_keyboards(*answers),
    )


@router.message(F.text.lower() == "menu")
async def menu(message: types.Message):
    await message.answer(text="Menu", reply_markup=kurs_keybinds)