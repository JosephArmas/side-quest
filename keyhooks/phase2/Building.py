from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

class Building(Base):
    __tablename__ = "buildings"
    building_name = Column('building_name', String, nullable = False, primary_key=True)

    # room = relationship('Room', back_populates='building')
    # rooms = relationship('Room', backref='buildings')



    def __init__(self, building_name: String):
        self.building_name = building_name
