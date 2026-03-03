from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class CategoryORM(Base):
    __tablename__ = 'category'
    name: Mapped[str] = mapped_column(String)
    course_degree: Mapped[int] = mapped_column(Integer())

