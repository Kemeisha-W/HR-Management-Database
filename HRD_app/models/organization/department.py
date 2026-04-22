from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class Department(Base):
    __tablename__ = "departments"
    code = Column(String, primary_key=True)
    name = Column(String)
    #Foreign Keys
    division_code = Column(String, ForeignKey("division.code"),nullable=False)
    #relationships
    division = relationship("Division",back_populates="departments")
    job = relationship("Job",back_populates="departments")

    #Utility Methods
    def __repr__(self):
        return f"<Department(code='{self.code}', name='{self.name}')>"