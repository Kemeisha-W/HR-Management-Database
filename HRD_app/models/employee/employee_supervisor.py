from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship 
from HRD_app.database import Base   

class EmployeeSupervisor(Base):
    __tablename__ = "employee_supervisor"
    id = Column(Integer,primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    supervisor_id = Column(Integer, ForeignKey("Employee.id"))

    supervisor_id = relationship("Employee", back_populates="EmployeeSupervisor")

    #Utility Methods
    def __repr__(self):
        return f"<EmployeeSupervisor(id={self.id}, start_date={self.start_date}, end_date={self.end_date}, supervisor_id={self.supervisor_id})>"
