from sqlalchemy import Column, String, UniqueConstraint, Identity , Integer, Date, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base
from Loan import Loan


class Key_Return(Base):
    __tablename__ = 'key_returns'
    return_date = Column('return_date', Date, nullable = False)

    # TODO add key_id attribute imported from loans
    loans_key_id = Column('loans_key_id', Integer, nullable = False, primary_key = True)

    # TODO add emp id attribute imported from loans
    loans_employee_id = Column('loans_employee_id', Integer, nullable = False, primary_key = True)

    # TODO add room num attribute imported from loans
    loans_room_number = Column('loans_room_number', Integer, nullable = False, primary_key = True)

    loans_building_name = Column('loans_building_name', String ,nullable = False, primary_key = True)
    
    # TODO add request date attributee from loans
    loans_request_date = Column('loans_request_date', Date, nullable = False, primary_key = True)

    __table_args__ = (ForeignKeyConstraint(['loans_key_id','loans_employee_id', 'loans_room_number', 'loans_building_name', 'loans_request_date'], ['loans.key_id','loans.employee_id', 'loans.room_number', 'loans.building_name', 'loans.date_requested'], ),)

    return_loans = relationship("Loan", backref='returned_loans')
    def __init__(self, return_date: Date, loans_key_id: Integer, loans_employee_id: Integer, loans_room_number: Integer, loans_building_name: String, loans_request_date: Date):
        self.return_date = return_date
        self.loans_key_id = loans_key_id
        self.loans_employee_id = loans_employee_id
        self.loans_room_number = loans_room_number
        self.loans_building_name = loans_building_name 
        self.loans_request_date = loans_request_date