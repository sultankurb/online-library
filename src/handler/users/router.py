from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.keyboards import create_keyboards
from .depends import get_lesson_names
from src.fsm.lessons import SelectLessons

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
keybinds_lst = [
    "Jeke tártiptegi kiyim tıgıwshısı",
    "Shashtarez (modelleri)",
    "Elektrik",
    "Baylanıs Operatori",
    "Xabar qurallari mashinaları hám kompyuter tarmaqları operatori",
    "Avtomobillerdi onlaw hám olarga texnik xizmet kòrsetiw",
    "Menu"
]

kurs_keybinds = create_keyboards("1-kurs", "2-kurs",)

@router.message(Command(commands="start", prefix="/"))
async def start_command(message: types.Message, state: FSMContext):
    await message.answer(text="Ассалаума алейкум", reply_markup=kurs_keybinds)
    await state.set_state(SelectLessons.course)
