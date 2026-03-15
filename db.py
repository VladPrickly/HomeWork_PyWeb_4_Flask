import atexit
from datetime import datetime
import os
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

class Base(DeclarativeBase):
    id: MappedColumn[int] = mapped_column(Integer, primary_key=True, autoincrement=True)


class Advertisement(Base):
    __tablename__ = 'advertisements'

    title: MappedColumn[str] = mapped_column(String)#, nullable=False, index=True)
    description: MappedColumn[str] = mapped_column(Text)#, nullable=True)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, server_default=func.now())
    owner: MappedColumn[str] = mapped_column(String)#, nullable=True)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'owner': self.owner
        }


Base.metadata.create_all(bind=engine)

atexit.register(engine.dispose)

