from sqlalchemy import Column, Integer, String, ForeignKey
from database.models.base import Base
from sqlalchemy.orm import relationship
from database.models.rolespermissions import roles_permissions_table


class Permite(Base):
    __tablename__ = 'permites'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    permite = Column('permite', String)
    roles = relationship('Role', secondary=roles_permissions_table, back_populates='permites')
