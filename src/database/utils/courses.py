from src.database.redis import client

async def save_user_course(telegram_id: int, course: str):
    await client.set(name=telegram_id, value=course)

async def get_course(telegram_id: int):
    return await client.get(name=telegram_id)
