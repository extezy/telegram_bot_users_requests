from aiogram import types
from loader import dispatcher
from loguru import logger


@logger.catch
@dispatcher.message_handler(state="full_name")
async def get_full_name(message: types.Message) -> None:
    logger.info(f"User_id: {message.from_user.id} use full_name state with message: {message.text}")
    full_name = None

    if message.text is not None:
        full_name = message.text.split()

    if len(full_name) == 2 and (full_name[0].isalpha() and full_name[1].isalpha()):
        # TODO запомнить имя используя  БД
            pass
    else:
        pass

