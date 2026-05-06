from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship 
from HRD_app.database import Base

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    hire_date = Column(Date)
    birth_date = Column(Date)
    phone_number = Column(Integer)
    email = Column(String)
    location = Column(Integer,ForeignKey("Location.id"))
    job = Column(String,ForeignKey("Job.code"))
    status_id = Column(String, ForeignKey("EmployeeStatus.id"))
    emp_type = Column(String, ForeignKey("EmployeeType.id"))
    anniversary = Column(Integer,ForeignKey("AnniversaryType.id"))
    contract = Column(String,ForeignKey("Contract.id"))
   
    #relationships
    contract = relationship("Contract", back_populates= "Employee")
    system_user = relationship("SystemUser", back_populates= "Employee")
    position_history = relationship("PositionHistory",back_populates="Employee")
    sep_details = relationship("SeparationDetail", back_populates="Employee")
    status_history = relationship("StatusHistory", back_populates="Employee")
    acting_assignment = relationship("ActingAssignment", back_populates="Employee")
    audit_log = relationship("AuditLog", back_populates="Employee")
    anniversary = relationship("AnniversaryType", back_populates= "Employee")
    emp_type = relationship("EmployeeType", back_populates= "Employee")
    status_id = relationship("EmployeeStatus",back_populates="Employee")
    job = relationship("Job", back_populates= "Employee")
    location = relationship("Location", back_populates= "Employee")

    #Utility Methods
    def __repr__(self):
        return f"<Employee(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})>"
    
