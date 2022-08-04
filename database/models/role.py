from sqlalchemy import Column, Integer, String
from database.models.base import Base
from sqlalchemy.orm import relationship
from database.models.rolespermissions import roles_permissions_table


class Role(Base):
    """
    Класс  для описания "Роли" в БД
    """
    __tablename__ = 'roles'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    role = Column('role', String)
    permissions = relationship('Permission', secondary=roles_permissions_table, back_populates='roles')
