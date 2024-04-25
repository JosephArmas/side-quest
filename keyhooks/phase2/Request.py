from sqlalchemy import Column, Integer, Identity, Float, ForeignKey,String, Date, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

from Employee import Employee
from Room import Room

class Request(Base):
    __tablename__ = 'requests'
    employee_id = Column('employee_id', Integer ,ForeignKey('employees.employee_id'),nullable = False, primary_key=True)
    date_requested = Column('date_requested', Date, primary_key=True )
    room_number = Column('room_number', Integer, nullable = False, primary_key=True)
    building_name = Column('building_name', String, nullable=False, primary_key=True)
    table_args= UniqueConstraint('employee_id','room_number','building_name')

    __table_args__ = (ForeignKeyConstraint(['room_number', 'building_name'],['rooms.room_number', 'rooms.building_name'],),)
    """ 
    fk_id = relationship('Employee', foreign_keys=[employee_id])
    room = relationship('Room', foreign_keys = [room_number])
    building = relationship('Room', foreign_keys = [building_name])
    """
    employees = relationship("Employee", backref='employees_room')
    rooms = relationship("Room", backref='rooms_employees')
    

    def __init__(self, employee_id: Integer, date_requested: Date, room_number: Integer, building_name: String):
        self.employee_id = employee_id
        self.date_requested = date_requested
        self.room_number = room_number
        self.building_name = building_name
