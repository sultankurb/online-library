from src.database.repository.repository import SQLAlchemyRepository
from src.database.models.lessons import LessonORM

class LessonsRepository(SQLAlchemyRepository):
    pass


lesson = LessonsRepository(model=LessonORM)


async def get_lesson_names(course_degree: int, course: str):
    result = []
    answers = await lesson.select_all(filters={'course_degree': course_degree, "course": course})
    for answer in answers:
        result.append(answer['name'])
        return result
    return None
