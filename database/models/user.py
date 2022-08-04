from sqlalchemy import Column, Integer, String, ForeignKey
from database.models.base import Base
from sqlalchemy.orm import relationship


class User(Base):
    """
    Класс  для описания "Пользователя" в БД
    """
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    priority = Column(Integer, ForeignKey('roles.id'))
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    username = Column('username', String)
    user_id = Column('user_id', Integer)
    phone_number = Column('phone_number', String)
    role = relationship("Role")

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}, priority: {self.priority}, phone: {self.phone_number}'

    def full_name(self) -> str:
         return f'{self.last_name} {self.first_name}'

    def set_full_name(self, values: list):
        self.last_name = values[0]
        self.first_name = values[1]
