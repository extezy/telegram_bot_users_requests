from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config_data import config
from loguru import logger
from config_data.config import DATABASE
from sqlalchemy import create_engine
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database.models.base import Base


engine = create_engine(f"sqlite:///{DATABASE}")
Base.metadata.create_all(engine) # Создаем все табилцы если их нет
logger.debug(f'Engine: {engine}')
bot = Bot(token=config.BOT_TOKEN)
logger.debug(f'Bot: {bot}')
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
logger.debug(f'Dispatcher: {dispatcher}')

