from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class PositionHistory(Base):
    __tablename__="position_history"
    id = Column(Integer, primary_key= True)
    employee_id = Column( Integer, ForeignKey("employee.id"))
    job_code = Column(String, ForeignKey("job.job_code"))
    start_date = Column(Date)
    end_date = Column(Date)
    position_type = Column(String)

    #relationships
    employee = relationship("Employee", back_populates="position_history")
    job = relationship("Job", back_populates="position_history")

    #Define Utility
    def __repr__(self):
        return f"<PositionHistory(id={self.id}, employee_id={self.employee_id}, job_code={self.job_code}, start_date={self.start_date}, end_date={self.end_date}, position_type={self.position_type})>"