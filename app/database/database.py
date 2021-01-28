from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/fakedata"
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
metadata = MetaData()


def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() 
