from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.settings import settings


engine = create_async_engine(url=settings.DB_URL)
session = async_sessionmaker(bind=engine)