from sqlalchemy import Column, Integer, String
from database.models.base import Base


class Address(Base):
    """
    Класс  для описания адреса в БД
    """
    __tablename__ = 'addresses'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    city = Column('city', String)
    street = Column('street', String)
    house = Column('house', Integer)
    flat = Column('flat', Integer)
    user_id = Column('user_id', Integer) # FOREIGN KEY user-user_id
