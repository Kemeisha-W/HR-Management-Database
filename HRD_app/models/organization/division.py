from sqlalchemy import Column,ForeignKey,Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Division(Base):
    __tablename__ = "divisions"
    code = Column(String, primary_key=True)
    name = Column(String)
    #Foreign Keys
    company_code = Column(String, ForeignKey("company.code"),nullable=False)
    #Relationships
    company = relationship("Company",back_populates="divisions")
    department = relationship("Departments",back_populates="divisions")

    #Utility Methods
    def __repr__(self):
        return f"<Division(code={self.code}, name={self.name})>"