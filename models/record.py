from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Date
from sqlalchemy.orm import relationship

from database import Base


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    type = Column(String(255))

    date_of_birth = Column(Date)
    date_purchased = Column(Date)
    vaccination_info = Column(Text)
    tag_colour = Column(String(255))
    number_of_kids = Column(Integer)
    colour = Column(String(255))

    #-------------------
    sire = Column(Integer, ForeignKey("records.id"), nullable=True)
    dam = Column(Integer, ForeignKey("records.id"), nullable=True)
    #--------------------
    #-----------------
    sire_children = relationship("Record", backref="s_parent", foreign_keys=[sire], remote_side=[id])

    dam_children = relationship("Record", backref="d_parent", foreign_keys=[dam], remote_side=[id])

    #--------------------
    #--------------------
    weight = Column(Text)
    castrated = Column(Boolean, default=False)
    health_condition = Column(Text)
    remarks = Column(Text)
    gender = Column(Enum('male', 'female'))

    date_of_birth = Column(Date)
    date_purchased = Column(Date)
    vaccination_info = Column(Text)
    alive = Column(Boolean, default=True)
    sold = Column(Boolean, default=False)




