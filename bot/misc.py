import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.executor import Executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN


logging.basicConfig(level=logging.INFO)
logging.getLogger('gino').setLevel(logging.WARNING)
bot = Bot(BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())
executor = Executor(dp, skip_updates=True)
