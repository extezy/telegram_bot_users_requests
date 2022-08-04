from sqlalchemy import Column, Integer, String, ForeignKey, Table
from database.models.base import Base


roles_permites_table = Table(
    "roles_permites",
    Base.metadata,
    Column('role_id', ForeignKey('roles.id'), primary_key=True),
    Column('permite_id', ForeignKey('permites.id'), primary_key=True),
)
