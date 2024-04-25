from sqlalchemy import Column, String, UniqueConstraint, Identity, ForeignKey, Integer, Date, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
# TODO import request file
from Request import Request
# TODO import keys file
from Key import Key
class Loan(Base):
    __tablename__ = 'loans'
    # TODO add keys attribute from keys table
    key_id = Column('key_id', Integer, ForeignKey('keys.key_id'),nullable=False, primary_key = True)

    # TODO add emp id from request table 
    employee_id = Column('employee_id', Integer,nullable=False ,primary_key = True)

    # TODO add date from request table 
    date_requested = Column('date_requested', Date, nullable=False, primary_key = True)

    # TODO add date from request table 
    room_number = Column('room_number', Integer, nullable=False, primary_key = True)

    # TODO add date from request table 
    building_name = Column('building_name', String, nullable=False, primary_key = True)

    __table_args__ = (ForeignKeyConstraint(['employee_id', 'date_requested', 'room_number', 'building_name'], ['requests.employee_id', 'requests.date_requested', 'requests.room_number', 'requests.building_name'], ), )

    requests = relationship("Request", backref='loans_requests')
    keys = relationship("Key", backref='loans_keys')

    def __init__(self, key_id: Integer, employee_id: Integer, date_requested: Date, room_number: Integer, building_name: String):
        self.key_id = key_id
        self.employee_id = employee_id
        self.date_requested = date_requested
        self.room_number = room_number
        self.building_name = building_name
        
