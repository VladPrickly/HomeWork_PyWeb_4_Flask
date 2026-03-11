import atexit
import datetime
import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase, MappedColumn, mapped_column
from sqlalchemy import create_engine, Integer, Text, String, DateTime, Column, func

POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "1234")
POSTGRES_DB = os.getenv("POSTGRES_DB", "netology_test_db")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5431)


PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

# Base = declarative_base(bind=engine)

class Base(DeclarativeBase):

    id = Column(Integer, primary_key=True, autoincrement=True)

class Advertisement(Base):

    __tablename__ = 'advertisements'

    title = Column(String, nullable=False, index=True)
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    author = Column(String)

Base.metadata.create_all(bind=engine)

atexit.register(engine.dispose)

