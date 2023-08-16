from sqlalchemy import Column, INTEGER, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"
    user_id = Column(INTEGER, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
