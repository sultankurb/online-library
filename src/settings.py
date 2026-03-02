from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
    )
    BOT_TOKEN: str = ''
    DB_URL: str = ''


def get_settings() -> Settings:
    return Settings()

settings = get_settings()
