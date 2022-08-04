import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

ROOT_DIR = os.path.dirname(os.path.abspath('__main__'))
BOT_TOKEN = os.getenv('BOT_TOKEN')
DATABASE = os.path.join(ROOT_DIR, 'database', 'requests_base.db')

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
)

DEFAULT_ROLES = (
    'quest',
    'user',
    'moderator',
    'admin'
)

DEFAULT_PERMISSIONS = {
    'quest': [('registration', 'Регистрация пользователя')],
    'user': [('change_information', 'Изменение личных данных'),
             ('create_request', 'Задать вопрос'),
             ('delete_request', 'Удалить вопрос')],
    'moderator': [('change_information', 'Изменение личных данных'),
                  ('create_request', 'Задать вопрос'),
                  ('delete_request', 'Удалить вопрос'),
                  ('set_answer', 'Ответить на вопрос'),
                  ('delete_answer', 'Удалить ответ на вопрос')],
    'admin': [('all_permissions', 'Можно всё и чуточку больше')]
}
