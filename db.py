import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_USER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST=os.getenv("POSTGRES_HOST")
POSTGRES_PORT=os.getenv("POSTGRES_PORT")

engine = create_engine()
