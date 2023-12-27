from sqlalchemy import  Boolean, Column, Integer, String
from database import Base


class Todos(Base):
    __tablename__ = "user"

    # userid = Column(Integer, primary_key=True),
    username = Column(String, primary_key=True, unique=True)
    password = Column(String)



