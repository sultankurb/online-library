from aiogram.fsm.state import State, StatesGroup


class Lessons(StatesGroup):
    name: str = State()
    file: str = State()
    category_pk: int = State()
