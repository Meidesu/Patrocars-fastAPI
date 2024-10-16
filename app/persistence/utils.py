import os
from sqlmodel import create_engine

database_url = os.getenv("DATABASE_URL")


def get_engine():
    """
    Creates and returns a SQLAlchemy engine instance.

    This function initializes a SQLAlchemy engine using the provided database URL.
    The engine is used to interact with the database.

    Returns:
        sqlalchemy.engine.Engine: An instance of SQLAlchemy engine connected to the specified database.
    """
    engine = create_engine(database_url)
    return engine
