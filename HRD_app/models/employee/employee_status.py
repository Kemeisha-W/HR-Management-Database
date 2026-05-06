from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class EmployeeStatus(Base):
    __tablename__ = "employee_status"
    id = Column(String,primary_key=True)
    name = Column(String)

    employee = relationship("employee",back_populates="EmployeeStatus")

    #Utility Method
    def __repr__(self):
        return f"EmployeeStatus(id={self.id}, name={self.name})"