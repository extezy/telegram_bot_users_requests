from aiogram import types
from loader import dispatcher
from loguru import logger
from database.services.mysession import session_scope
from database.models.user import User
from database.models.role import Role
from keyboards.start_keyboard import get_start_keyboard


@logger.catch
# @dispatcher.message_handler(commands="start")
async def start(message: types.Message):
    """
    Обработчик команды /start
    """
    logger.info(f"User_id: {message.from_user.id} use /start command")
    with session_scope() as session:
        user_id = message.from_user.id
        quest = session.query(Role).filter_by(role='quest').one()
        user = session.query(User).filter_by(user_id=user_id).one()
        if user is None:
            user = User()
            user.user_id = user_id
            user.username = message.from_user.username
            user.role = quest
            session.add(user)
            await message.reply(
                f"Здравствуйте, {message.from_user.full_name.capitalize()}! \nДля использования сервиса Вам необходимо зарегестрироваться!\n /registration", reply_markup=get_start_keyboard(user=user))
        elif user.role == quest:
            await message.reply(
                f"Здравствуйте, {message.from_user.full_name.capitalize()}! \nДля использования сервиса Вам необходимо зарегестрироваться!\n /registration",
                reply_markup=get_start_keyboard(user))
        else:
            await message.reply(
                f"Добро пожаловать, {user.full_name()}! \nЧто бы Вы хотели сделать?!", reply_markup=get_start_keyboard(user=user))
