from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session
from loader import engine
from loguru import logger


@logger.catch
@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
