"""Database session configuration."""

from collections.abc import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

# from simpsonapi_playground.core.db import Base

from simpsonapi_playground.core.config import DATABASE_URL

load_dotenv()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Generator[Session, None, None]:
    """Dependency function that provides a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def create_tables():
#     Base.metadata.create_all(bind=engine)
