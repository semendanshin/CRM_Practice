from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "User"
    telegram_id = Column(Integer, primary_key=True, unique=True)
    access_token = Column(String)
    

