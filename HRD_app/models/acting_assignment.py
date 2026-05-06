from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class ActingAssignment(Base):
    __tablename__ = "acting_assignments"
    id = Column(Integer,primary_key=True,autoincrement=True)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)
    is_current = Column(Boolean,nullable=False)
    employee = Column(Integer, ForeignKey("employee.id"))
    job = Column(String, ForeignKey("job.code"))

    #relationships
    job = relationship("Job", back_populates="ActingAssignment")
    employee = relationship("Employee", back_populates= "ActingAssignment")

    #Utility Methods
    def __repr__(self):
        return f"<ActingAssignment(id={self.id}, start_date={self.start_date}, end_date={self.end_date}, description='{self.description}', is_current={self.is_current})>"  