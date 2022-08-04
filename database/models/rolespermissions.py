from sqlalchemy import Column, Integer, String, ForeignKey, Table
from database.models.base import Base


roles_permissions_table = Table(
    "roles_permissions",
    Base.metadata,
    Column('role_id', ForeignKey('roles.id'), primary_key=True),
    Column('permission_id', ForeignKey('permissions.id'), primary_key=True),
)
