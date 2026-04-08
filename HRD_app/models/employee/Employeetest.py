from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base


class Employee(Base):
    __tablename__ = "employees"

    # 🔑 Primary Key
    id = Column(Integer, primary_key=True)

    # 👤 Basic Info
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))

    # 📅 Employment Info
    hire_date = Column(Date, nullable=False)

    # 🔗 Foreign Keys
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))

    status_id = Column(Integer, ForeignKey("employee_status.id"))
    employment_type_id = Column(Integer, ForeignKey("employment_types.id"))

    # 🔄 Relationships (VERY IMPORTANT)

    # Organization
    department = relationship("Department", back_populates="employees")
    job = relationship("Job", back_populates="employees")
    location = relationship("Location", back_populates="employees")

    # Classification
    status = relationship("EmployeeStatus", back_populates="employees")
    employment_type = relationship("EmploymentType", back_populates="employees")

    # 👨‍💼 Supervisor relationship (self-referencing)
    supervisor_id = Column(Integer, ForeignKey("employees.id"))
    supervisor = relationship("Employee", remote_side=[id], backref="subordinates")

    # 📜 History
    position_history = relationship("PositionHistory", back_populates="employee")
    status_history = relationship("StatusHistory", back_populates="employee")

    # 📄 Contracts
    contracts = relationship("EmployeeContract", back_populates="employee")

    # 🚪 Separation
    separation_details = relationship("SeparationDetails", back_populates="employee", uselist=False)

    # 🎭 Acting Role
    acting_assignment = relationship("ActingAssignment", back_populates="employee", uselist=False)

    # 📝 Audit
    audit_logs = relationship("AuditLog", back_populates="employee")

    # 🧠 Utility Methods

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<Employee(id={self.id}, name={self.full_name()}, email={self.email})>"