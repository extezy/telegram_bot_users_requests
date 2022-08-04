from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database.models.user import User
from loguru import logger


@logger.catch
def get_start_keyboard(user: User) -> ReplyKeyboardMarkup:
    """
    Функция для получения шаблона команд бота в  зависимости  от роли
    :return: набор стартовых кнопок с командами
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    permissions = user.role.permissions
    for permission in permissions:
        new_button = KeyboardButton(text=f'/{permission.permission}')
        markup.add(new_button)
    new_button = KeyboardButton(text='/help')
    markup.add(new_button)

    return markup
