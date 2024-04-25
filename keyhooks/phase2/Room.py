from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Building import Building

class Room(Base):
    __tablename__ = 'rooms'
    # room_id = Column('room_id', Integer, nullable=False, primary_key = True )
    room_number = Column('room_number', Integer, nullable = False, primary_key = True )
    building_name = Column('building_name', String, ForeignKey('buildings.building_name'), nullable = False, primary_key = True) 
    __table_args__ = (ForeignKeyConstraint(['building_name'],['buildings.building_name'],),)
    # table_args = (UniqueConstraint('room_number', 'building_name', name='rooms_uk_01'))
    # tabe_args = UniqueConstraint('room_number', 'building_name')
    buildings = relationship("Building", backref="rooms_building")

    def __init__(self,room_number: Integer, building_name: String):
        # self.room_id = room_id
        self.room_number = room_number
        self.building_name = building_name
