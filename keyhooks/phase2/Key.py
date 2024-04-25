from sqlalchemy import Column, Integer, Identity, Float, \
    String, UniqueConstraint, ForeignKeyConstraint, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

from Hook import Hook

class Key(Base):
    __tablename__ = 'keys'
    key_id = Column('key_id', Integer, nullable = True, primary_key = True)
    hook_id = Column('hook_id', Integer, ForeignKey('hooks.hook_id'), nullable = False)


    def __init(self, key_id: Integer, hook_id: Integer):
        self.key_id = key_id
        self.hook_id = hook_id
