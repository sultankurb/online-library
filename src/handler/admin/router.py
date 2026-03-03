from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from src.database.repository import category
from src.fsm.category import Category

from src.middleware.admin import ADMINMiddleware
from src.settings import settings

router = Router()
# router.message.middleware(ADMINMiddleware(admin_id=settings.ADMIN_ID))


@router.message(StateFilter(None), F.text == "add course")
async def add_course(message: types.Message, state: FSMContext):
    await message.answer(
        "send name"
    )
    await state.set_state(Category.name)


@router.message(Category.name, F.text)
async def set_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text="input course degree")
    await state.set_state(Category.course_degree)


@router.message(Category.course_degree, F.text)
async def set_course_degree(message: types.Message, state: FSMContext):
    await state.update_data(course_degree=message.text)
    data = await state.get_data()
    course_degree = int(data["course_degree"])
    name: str = data["name"]
    full_name: str = name + f"_V{course_degree}"
    await category.insert_one(data={"course_degree": course_degree, "name": full_name})
    await state.clear()

