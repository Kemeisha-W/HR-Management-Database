from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer,primary_key=True)
    address = Column(String)
    city = Column(String)
    country = Column(String)
    postal_code = Column(String)

    #relationships
    company = relationship("Company", back_populates= "location")
    employees = relationship("Employee", back_populates="location")

    #utility method
    def __repr__(self):
        return f"Location(id={self.id}, address='{self.address}', city='{self.city}', country='{self.country}', postal_code='{self.postal_code}')"