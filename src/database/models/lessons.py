from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class LessonORM(Base):
    __tablename__ = "lessons"
    name: Mapped[str] = mapped_column(String())
    file_url: Mapped[str] = mapped_column(String(length=2048), nullable=False)
    category: Mapped[int] = mapped_column(ForeignKey('category.pk'), nullable=False)
