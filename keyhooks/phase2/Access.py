from sqlalchemy import Column, Integer, Identity, Float, \
    String, Date, UniqueConstraint, ForeignKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Hook import Hook
from Door import Door

class Access(Base):
    __tablename__ = 'access'
    hook_id = Column('hook_id', Integer, ForeignKey('hooks.hook_id'), primary_key=True)
    room_number = Column('room_number', Integer, primary_key=True)
    building_name = Column('building_name', String, primary_key=True)
    door_type= Column('door_type', String, primary_key=True)
    __table_args__ = (ForeignKeyConstraint(['room_number', 'building_name', 'door_type'],['doors.room_number', 'doors.building_name', 'doors.door_type'], ),)


    hooks = relationship('Hook', backref='access_hooks')
    doors = relationship('Door', backref='access_doors')

    def __init__(self, hook_id: Integer, room_number: Integer, building_name: String, door_type: String):
        self.hook_id = hook_id
        self.room_number = room_number
        self.building_name = building_name
        self.door_type = door_type
