from sqlalchemy import Column,ForeignKey,Integer, String
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class EmployeeType(Base):
    __tablename__ = "employee_type"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    employee = relationship("employee",back_populates="EmployeeType")

    #Utility Methods
    def __repr__(self):
        return f"<EmployeeType(id={self.id}, name={self.name})>"