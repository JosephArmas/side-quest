from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

class Door_Type(Base):
    __tablename__ = 'door_types'
    type = Column('type', String(20), nullable = False, primary_key = True)


    def __init__(self, type: String):
        self.type = type
