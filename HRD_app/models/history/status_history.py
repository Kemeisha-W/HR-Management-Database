from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class StatusHistory(Base):
    __tablename__ = "status_history"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    status_id = Column(Integer, ForeignKey("status.id"))
    start_date = Column(Date)
    end_date = Column(Date)

    #relationships
    employee = relationship("Employee", back_populates="status_history")
    status = relationship("EmployeeStatus", back_populates = "status_history")

    #Define Utility
    def __repr__(self):
        return f"<StatusHistory(id={self.id}, employee_id={self.employee_id}, status_id={self.status_id}, start_date={self.start_date}, end_date={self.end_date})>"