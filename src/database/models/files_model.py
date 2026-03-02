from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer

from .base import  Base


class FilesORM(Base):
    __tablename__ = "files"
    file_url: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    course_degree: Mapped[int] = mapped_column(Integer())
