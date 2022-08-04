from sqlalchemy import Column, Integer, String
from Base import get_base
from loader import engine


class User(get_base()):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    priority = Column('priority', Integer)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    chat_id = Column('chat_id', Integer)
    phone_number = Column('phone_number', String)

    get_base().metadata.
