from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    type = Column(String(255))
    #type multichoice
    #date created
    #vaccination info
    tag_colour = Column(String(255))
    number_of_kids = Column(Integer)
    colour = Column(String(255))
    #sire
    #dam
    #gender multi choice
    castrated = Column(Boolean, default=False)
    health_condition = Column(String(255))
    remarks = Column(String(255))


