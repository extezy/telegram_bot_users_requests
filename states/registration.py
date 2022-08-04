from aiogram import types
from aiogram.dispatcher import Dispatcher
from loguru import logger
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.contact import get_share_contact_keyboard
from database.services.mysession import session_scope
from database.models.user import User
from database.models.role import Role
from keyboards.start_keyboard import get_start_keyboard


class FSMRegistration(StatesGroup):
    full_name = State()
    phone_number = State()


@logger.catch
# @dispatcher.message_handler(content_types=['text'], state=FSMRegistration.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    """
    Обработчик состояния "full_name", сценария "Регистрация  пользователя"
    """
    async with state.proxy() as data:
        logger.info(f"User_id: {message.from_user.id} use full_name state with message: {message.text}")
        full_name = None

        if message.text.isprintable():
            full_name = message.text.split()

        if len(full_name) == 2 and (full_name[0].isalpha() and full_name[1].isalpha()):
            data['full_name'] = full_name
            await FSMRegistration.next()
            await message.reply('Ваш номер телефона',  reply_markup=get_share_contact_keyboard())


@logger.catch
# @dispatcher.message_handler(content_types=['contact'], state=FSMRegistration.phone_number)
async def get_contact(message: types.Message, state: FSMContext):
    """
    Обработчик состояния "phone_number", сценария "Регистрация  пользователя"
    """
    logger.info(f"User_id: {message.from_user.id} use phone_number state with message: {message.contact}")
    async with state.proxy() as data:
        with session_scope() as session:
            user_role = session.query(Role).filter_by(role='user').first()
            user = session.query(User).filter(User.user_id == message.from_user.id).first()
            user.set_full_name(data.get(value='full_name'))
            user.phone_number = message.contact.phone_number
            user.role = user_role
            session.add(user)
            await message.reply('Регистрация успешна!', reply_markup=get_start_keyboard(user))
    await state.finish()


def set_registration_states(dispatcher: Dispatcher):
    """
    Функция для добавления обработчиков событий сценария "Регистрация  пользователя"
    :param dispatcher:
    :return:
    """
    dispatcher.register_message_handler(get_full_name, content_types=['text'], state=FSMRegistration.full_name)
    dispatcher.register_message_handler(get_contact,
                                        content_types=types.ContentType.CONTACT, state=FSMRegistration.phone_number)
