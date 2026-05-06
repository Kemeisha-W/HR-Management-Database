from pathlib import Path
import sqlalchemy as sa
from sqlalchemy import Column,JSON,ForeignKey,Integer, String, Table, Float,Date,Boolean,LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db_path = Path(__file__).resolve().parent/"HR_db"
engine = sa.create_engine(f"sqlite:///{db_path}",echo=True,future = True)

Base = declarative_base()
Session = sessionmaker(bind = engine, autoflush=False, autocommit=False, future=True)
session = Session()
