from sqlalchemy import Column, String, UniqueConstraint, Identity, ForeignKey, Integer, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base

class Employee(Base):
    __tablename__ = 'employees'
    employee_id = Column('employee_id', Integer, nullable = False, primary_key = True)
    # requests = relationship('Request', backref='employees')
    # requests = relationship('Request', foreign_keys = 'Employee.employee_id')
    def __init__(self, employee_id: Integer):
        self.employee_id = employee_id
