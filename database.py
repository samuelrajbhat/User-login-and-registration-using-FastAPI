# create_engine is a module that establishes the connection between python object and database table

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Db_url = 'postgresql://postgres:1234@localhost:5432/Users'
# database_url_object(variable) = "DBMS_name://Db_username:Paswwrord@port_addres/database name"

engine = create_engine(Db_url)
# create_engine takes Db_url as a parameter to set up connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


