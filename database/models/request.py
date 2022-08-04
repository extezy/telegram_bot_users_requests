from sqlalchemy import Column, Integer, String, ForeignKey
from database.models.base import Base
from sqlalchemy.orm import relationship


class Request(Base):
    """
    Класс  для описания "Вопроса" в БД
    """
    __tablename__ = 'requests'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    user_problem = Column('user_problem', String)
    user_id = Column(Integer, ForeignKey('users.id')) # FOREIGN KEY user-user_id  user_id = Column(Integer, ForeignKey('user.id'))
    executor_id = Column(Integer, ForeignKey('users.id'))  # FOREIGN KEY user-user_id
    executor_answer = Column('executor_answer', String)

    user = relationship("User", foreign_keys=[user_id])
    executor = relationship("User", foreign_keys=[executor_id])
