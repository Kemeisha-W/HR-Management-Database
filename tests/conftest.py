import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from pathlib import Path
from HRD_app.database import Base

#create database engine
@pytest.fixture(scope="session")
def db_engine():
    db_engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(db_engine)
    return db_engine

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
def db_session(connection):  
    session = sessionmaker(bind=connection)
    session = Session()
    try:
        yield session
    finally:
        session.close()