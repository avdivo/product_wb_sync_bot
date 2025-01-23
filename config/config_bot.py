from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

from config.config import Config
from bot.handlers import register_handlers


bot = Bot(token=Config.BOT_TOKEN)
router = Router()
register_handlers(router)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(router)
