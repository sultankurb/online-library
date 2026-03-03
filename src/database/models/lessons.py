from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class LessonORM(Base):
    __tablename__ = "lessons"
    name: Mapped[str] = mapped_column(String())
    course: Mapped[str] = mapped_column(String(length=1024))
    course_degree: Mapped[int] = mapped_column(Integer(), nullable=False)
    file_url: Mapped[str] = mapped_column(String(length=2048), nullable=False)
