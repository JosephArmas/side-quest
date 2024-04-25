from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Room import Room
from Door_Type import Door_Type

#broken atm
class Door(Base):
    __tablename__ = 'doors'
    room_number = Column('room_number', Integer, nullable=False,primary_key = True)
    building_name = Column('building_name', String, nullable=False, primary_key = True)
    door_type = Column('door_type', String, ForeignKey('door_types.type'), nullable=False, primary_key = True) 
    __table_args__ = (ForeignKeyConstraint(['room_number', 'building_name'], ['rooms.room_number', 'rooms.building_name'], ),)
    rooms = relationship('Room', backref='doors_rooms')
    doors_typess = relationship('Door_Type', backref='doorss_types')



    def __init__(self, room_number, building_name, door_type):
        self.room_number = room_number
        self.building_name = building_name
        self.door_type = door_type