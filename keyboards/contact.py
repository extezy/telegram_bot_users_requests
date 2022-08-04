from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


markup = ReplyKeyboardMarkup(resize_keyboard=True)

contact_button = KeyboardButton(text="Share", request_contact=True)

markup.add(contact_button)


def get_share_contact_keyboard() -> ReplyKeyboardMarkup:
    """
    Функция для получения шаблона команды бота
    :return: шаблон для ввода контакта
    """
    return markup
