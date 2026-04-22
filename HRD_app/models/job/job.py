from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class Job(Base):
    __tablename__ = "jobs"
    code = Column(String, primary_key=True)
    title = Column(String)
    grade = Column(String, ForeignKey("grade.code"))
    grade = relationship("Grade", back_populates="jobs")
    min_salary = Column(Float)
    max_salary = Column(Float)
    departments_code = Column(String,ForeignKey("department.code"),nullable=False)
    departments = relationship("Departments",back_populates="jobs")
    acting_assignment = relationship("ActingAssignment", back_populates="job")

    #Utility Methods
    def __repr__(self):
        return f"<Job(code='{self.code}', title='{self.title}')>"