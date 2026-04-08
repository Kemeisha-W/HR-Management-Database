from pathlib import Path
from sqlalchemy import create_engine,Column,JSON,ForeignKey,Integer, String, Table, Float,Date,Boolean,LargeBinary
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db_path = Path(__file__).resolve().parent/"HR_db"
engine = create_engine(f"sqlite:///{db_path}",echo=True)

Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()

class Grade(Base):
    __tablename__ = "grade"
    code = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    job = relationship("Job", back_populates="grade")

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

class EmployeeStatus(Base):
    __tablename__ = "employee_status"
    id = Column(String,primary_key=True)
    name = Column(String)
    employee = relationship("employee",back_populates="EmployeeStatus")

class EmployeeType(Base):
    __tablename__ = "employee_type"
    id = Column(Integer,primary_key=True)
    name = Column(Integer)
    employee = relationship("employee",back_populates="EmployeeType")

class Contract(Base):
    __tablename__ = "contracts"
    id = Column(Integer,primary_key=True)
    probation_end_date = Column(Date)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)
    contract_type_id = Column(String, ForeignKey("ContractType.id"))
    contract_type_id = relationship("ContractType", back_populates="Contract")
    employee_id = Column(Integer, ForeignKey("employee.id"))
    employee_id = relationship("Employee", back_populates="Contract")

class ContractType(Base):
    __tablename__ = "contract_type"
    id = Column(String,primary_key=True)
    name = Column(String)
    duration = Column(String)
    contract = relationship("Contract", back_populates="ContractType")

class AnniversaryType(Base):
    __tablename__ = " anniversary_type"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    created_date = Column(Date)
    update_date = Column(Date)
    anniversary_date = Column(Date)
    created_by = Column(String)
    updated_by = Column(String)

class PositionHistory(Base):
    __tablename__ = "position_history"
    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    position_type = Column(String)
    employee = Column(Integer, ForeignKey("employee.id"))
    employee = relationship("Employee",back_populates="PositionHistory")
    job = Column(String, ForeignKey("Job.code"))
    job = relationship("Job",back_populates="PositionHistory")

class StatusHistory(Base):
    __tablename__= "status_history"
    id = Column(Integer, primary_key=True)
    status_date = Column(Date)
    end_date = Column(Date)
    employee = Column(Integer, ForeignKey("employee.id"))
    employee = relationship("Employee",back_populates="StatusHistory")
    status_id = Column(String, ForeignKey("EmployeeStatus.id"))
    status_id = relationship("EmployeeStatus",back_populates="StatusHistory")

class SeparationReason(Base):
    __tablename__ = "separation_reasons"
    id = Column(Integer,primary_key=True)
    description = Column(String)
    sep_details = relationship("SeparationDetail", back_populates="SeparationReason")

class SeparationDetail(Base):
    __tablename__ = "separation_details"
    id = Column(Integer,primary_key=True)
    separation_date = Column(Date)
    notes = Column(String)
    rehire_eligibility = Column(Boolean)
    employee_id = Column(Integer, ForeignKey("Employee.id"))
    employee_id = relationship("Employee", back_populates="SeparationDetail")
    reason_id = Column(Integer, ForeignKey("SeparationReason.id"))
    reason_id = relationship("SeparationReason", back_populates="SeparationDetail")

class EmployeeSupervisor(Base):
    __tablename__ = "employee_supervisor"
    id = Column(Integer,primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    supervisor_id = Column(Integer, ForeignKey("Employee.id"))
    supervisor_id = relationship("Employee", back_populates="EmployeeSupervisor")

class ActingAssignment(Base):
    __tablename__ = "acting_assignments"
    id = Column(Integer,primary_key=True,autoincrement=True)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)
    is_current = Column(Boolean,nullable=False)
    employee = Column(Integer, ForeignKey("employee.id"))
    employee = relationship("Employee", back_populates= "ActingAssignment")
    job = Column(String, ForeignKey("job.code"))
    job = relationship("Job", back_populates="ActingAssignment")

class SystemUser(Base):
    __tablename__ = "system_users"
    id = Column(Integer, primary_key = True)
    employee_id = Column(Integer,ForeignKey("employee.id"))
    employee_id = relationship("Employee", back_populates= "SystemUser")
    username = Column(Integer, nullable=False)
    password_harsh = Column(String, nullable=False)
    email = Column(String)
    role = Column(String,nullable=False)
    is_active = Column(Boolean,nullable=False)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    log_id = Column(Integer,primary_key=True)
    user_id = Column(Integer)
    timestamp = Column(Date)
    table_ref = Column(String)
    operation_type = Column(String)
    changed_by_user_id = Column(String)
    old_value = Column(JSON)
    new_value = Column(JSON)
    details = Column(String)
    user = Column(Integer,ForeignKey("system_users.id"),nullable=False)
    user = relationship("SystemUser",back_populates="AuditLog")

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
    location = relationship("Location", back_populates= "Employee")
    job = Column(String,ForeignKey("Job.code"))
    job = relationship("Job", back_populates= "Employee")
    status_id = Column(String, ForeignKey("EmployeeStatus.id"))
    status_id = relationship("EmployeeStatus",back_populates="Employee")
    emp_type = Column(String, ForeignKey("EmployeeType.id"))
    emp_type = relationship("EmployeeType", back_populates= "Employee")
    anniversary = Column(Integer,ForeignKey("AnniversaryType.id"))
    anniversary = relationship("AnniversaryType", back_populates= "Employee")
    contract = Column(String,ForeignKey("Contract.id"))
    contract = relationship("Contract", back_populates= "Employee")
    system_user = relationship("SystemUser", back_populates= "Employee")
    position_history = relationship("PositionHistory",back_populates="Employee")
    sep_details = relationship("SeparationDetail", back_populates="Employee")
    status_history = relationship("StatusHistory", back_populates="Employee")

session.commit()