from aiogram.utils import executor
from loader import dispatcher
from loguru import logger
from utils.set_bot_commands import set_default_commands
from database.services.set_default_roles_permissions import set_default_roles, set_default_permissions
from states.registration import set_registration_states
from database.services.mysession import session_scope


if __name__ == '__main__':

    logger.add("./logs/debug.log", format="{time} {level} {message}", level="DEBUG", rotation="50 MB", compression="zip")

    set_default_roles()
    set_default_permissions()
    set_default_commands(dispatcher=dispatcher)
    set_registration_states(dispatcher=dispatcher)

    try:
        executor.start_polling(dispatcher=dispatcher, skip_updates=True)
    except Exception as exception:
        logger.error(exception)
