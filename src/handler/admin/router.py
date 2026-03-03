from aiogram import Router, types, F
from aiogram.filters import Command
from src.middleware.admin import  ADMINMiddleware
from src.settings import  settings

router = Router()
router.message.middleware(ADMINMiddleware(admin_id=[settings.ADMIN_ID]))
