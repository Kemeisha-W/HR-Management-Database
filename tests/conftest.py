import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from pathlib import Path

#create database engine
@pytest.fixture(scope="session")
def db_engine():
    from HRD_app.database import Base    

    engine = create_engine("sqlite:///:memory:", echo=True)
    import HRD_app.models.load
    Base.metadata.create_all(engine)
    return engine

#create connection(once per test)
@pytest.fixture(scope ="function")
def connection(db_engine):
    conn = db_engine.connect()
    trans = conn.begin()
    try:
        yield conn
    finally:
        trans.rollback()
        conn.close()

@pytest.fixture(scope="function")
def session(connection):  
    session = sessionmaker(bind=connection)
    session = session()
    try:
        yield session
    finally:
        session.close()