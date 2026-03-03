from aiogram.fsm.state import State, StatesGroup


class Lessons(StatesGroup):
    name: str = State()
    course: str = State()
    course_degree: int = State()
    file: str = State()


class SelectLessons(StatesGroup):
    course: str = State()
    course_degree: int = State()
