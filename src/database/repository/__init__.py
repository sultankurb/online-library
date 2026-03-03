__all__ = ["lesson", "category"]

from src.database.models.lessons import LessonORM
from src.database.models.category import CategoryORM
from .repository import SQLAlchemyRepository

lesson = SQLAlchemyRepository(model=LessonORM)
category = SQLAlchemyRepository(model=CategoryORM)
