from sqlalchemy import Column, Integer, String, ForeignKey
from database.models.base import Base
from sqlalchemy.orm import relationship
from database.models.rolespermissions import roles_permissions_table


class Permission(Base):
    """
    Класс  для описания "Разрешения" в БД
    """
    __tablename__ = 'permissions'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    permission = Column('permission', String)
    description = Column('description', String)
    roles = relationship('Role', secondary=roles_permissions_table, back_populates='permissions')
