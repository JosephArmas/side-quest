from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from orm_base import Base


class Hook(Base):
    __tablename__ = "hooks"
    hook_id = Column('hook_id', Integer, nullable = False, primary_key=True)

    #needed to connect keys to hooks
    # keys = relationship('keys', backref='hooks')


    def __init__(self, hook_id: Integer):
        self.hook_id = hook_id
        # self.keys_list = []

