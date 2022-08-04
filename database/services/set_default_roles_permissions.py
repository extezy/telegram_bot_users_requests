from config_data.config import DEFAULT_ROLES
from loguru import logger
from database.services.mysession import session_scope
from database.models.role import Role


@logger.catch
def set_default_roles():
    with session_scope() as session:
        for role in DEFAULT_ROLES:
            if session.query(Role).filter_by(role=role).first() is False:
                new_role = Role()
                new_role.role = role
                session.add(new_role)


@logger.catch
def set_default_permissions():
    with session_scope() as session:
        for role in DEFAULT_ROLES:
            if session.query(Role).filter_by(role=role).first() is False:
                new_role = Role()
                new_role.role = role
                session.add(new_role)