from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from database import Base


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    type = Column(String(255))
    #date created
    #vaccination info
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

    castrated = Column(Boolean, default=False)
    health_condition = Column(String(255))
    remarks = Column(String(255))
    gender = Column(Enum('male', 'female'))




