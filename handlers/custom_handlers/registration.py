from aiogram import types
from loguru import logger
from states.registration import FSMRegistration
from database.services.mysession import session_scope
from database.models.user import User
from keyboards.start_keyboard import get_start_keyboard


@logger.catch
# @dispatcher.message_handler(commands="registration")
async def registration(message: types.Message):
    """
    Обработчик команды /registration
    """
    logger.info(f"User_id: {message.from_user.id} use /registration command")
    with session_scope() as session:
        user = session.query(User).filter_by(user_id=message.from_user.id).one()
        if user is None or user.role.role == 'quest':
            await FSMRegistration.full_name.set()
            await message.reply('Введите Фамилию Имя(через пробел)', reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.reply(f'{user.full_name()} Вы уже зарегестрированы!', reply_markup=get_start_keyboard(user=user))
