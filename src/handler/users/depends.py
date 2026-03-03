from src.database.repository import lesson, category


async def get_lesson_names(course_degree: int, course: str):
    result = []
    answers = await lesson.select_all(filters={'course_degree': course_degree, "course": course})
    for answer in answers:
        result.append(answer['name'])
        return result
    return None

async def get_all_courses_category(course_degree: int):
    result = []
    stmt = await  category.select_all(filters={'course_degree': course_degree})
    for names in stmt:
        result.append(names.name)
        return result
    return None
