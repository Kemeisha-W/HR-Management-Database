from sqlalchemy import Column,ForeignKey,Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from database import Base

class Company(Base):
    __tablename__ = "companies"
    code = Column(String, primary_key=True)
    name = Column(String)
    img = Column(LargeBinary)
    location_id = Column(Integer, ForeignKey("locations.id"),nullable=False)
    location = relationship("Location",back_populates="companies")
    division = relationship("Division",back_populates="companies")

    #Utility Methods
    def __repr__(self):
        return f"<Company(code={self.code}, name={self.name}, location_id={self.location_id})>"