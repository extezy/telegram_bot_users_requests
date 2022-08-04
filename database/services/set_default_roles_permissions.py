from config_data.config import DEFAULT_ROLES, DEFAULT_PERMISSIONS
from loguru import logger
from database.services.mysession import session_scope
from database.models.role import Role
from database.models.permission import Permission


@logger.catch
def set_default_roles():
    with session_scope() as session:
        for role in DEFAULT_ROLES:
            if session.query(Role).filter_by(role=role).first() is None:
                new_role = Role()
                new_role.role = role
                session.add(new_role)


@logger.catch
def set_default_permissions():
    with session_scope() as session:
        for role in DEFAULT_ROLES:
            for permission, description in DEFAULT_PERMISSIONS.get(role):
                role_from_base = session.query(Role).filter_by(role=role).first()
                if role_from_base:
                    new_permission = Permission()
                    new_permission.permission = permission
                    new_permission.description = description
                    if (permission in role_from_base.permissions) is False:
                        permission_from_base = session.query(Permission).filter_by(permission=permission).first()
                        if permission_from_base:
                            role_from_base.permissions.append(permission_from_base)
                        else:
                            role_from_base.permissions.append(new_permission)
