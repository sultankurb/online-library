from aiogram import types, BaseMiddleware
from typing import Awaitable, Callable, Dict, Any

class ADMINMiddleware(BaseMiddleware):
    def __init__(self, admin_id: int):
        self.admin_id = admin_id

    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id == self.admin_id:
            return await handler(event, data)
        return None
