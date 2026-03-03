from aiogram.fsm.state import State, StatesGroup


class Category(StatesGroup):
    name = State()
    course_degree = State()
