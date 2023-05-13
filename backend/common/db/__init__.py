from typing import Any, Generator
from backend.common.db.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(settings.db_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, Any, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
