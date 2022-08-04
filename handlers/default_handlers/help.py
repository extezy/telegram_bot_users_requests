from aiogram import types
from loader import dispatcher
from loguru import logger
from database.services.mysession import session_scope
from database.models.user import User
from database.models.role import Role
from keyboards.start_keyboard import get_start_keyboard


@logger.catch
# @dispatcher.message_handler(commands="help")
async def help(message: types.Message):
    """
    Обработчик команды /help
    """
    logger.info(f"User_id: {message.from_user.id} use /help command")
    with session_scope() as session:
        user = session.query(User).filter(User.user_id == message.from_user.id).one()

        if user is not None:
            if user.role.role != 'quest':
                text = f'Здравствуйте, {user.full_name()} для вас доступны следующие команды:'
                for permission in user.role.permissions:
                    text += f'\n/{permission.permission} - {permission.description}'
            else:
                text = f'Здравствуйте, {message.from_user.full_name} для вас доступны следующие команды:'
                for permission in user.role.permissions:
                    text += f'\n/{permission.permission} - {permission.description}'
        else:
            role = session.query(Role).filter_by(role='quest').one()
            user = User()
            user.user_id = message.from_user.id
            user.username = message.from_user.username
            user.role = role
            session.add(user)
            text = f'Здравствуйте, {message.from_user.full_name} для вас доступны следующие команды:'
            for permission in role.permissions:
                text += f'\n{permission.permission} - {permission.description}'
        text += '\n/help - Информация о доступных командах'
        await message.reply(text, reply_markup=get_start_keyboard(user))
