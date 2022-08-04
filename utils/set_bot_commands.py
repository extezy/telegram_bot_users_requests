from aiogram.types import BotCommand
from aiogram.dispatcher import Dispatcher
from config_data.config import DEFAULT_COMMANDS
from loguru import logger
from handlers.default_handlers import start, help
from handlers.custom_handlers import registration


@logger.catch
def set_default_commands(dispatcher: Dispatcher):

    dispatcher.register_message_handler(callback=start.start, commands="start", state=None)
    dispatcher.register_message_handler(callback=help.help, commands="help", state=None)
    dispatcher.register_message_handler(callback=registration.registration, commands="registration", state=None)

    dispatcher.bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
