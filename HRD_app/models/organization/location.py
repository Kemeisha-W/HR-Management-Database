from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer,primary_key=True)
    address = Column(String)
    city = Column(String)
    country = Column(String)
    postal_code = Column(String)

    #relationships
    company = relationship("Company", back_populates= "locations")
    employees = relationship("Employee", back_populates="location")