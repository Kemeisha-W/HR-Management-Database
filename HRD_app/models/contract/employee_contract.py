from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class EmployeeContract(Base):
    __tablename__ = 'employee_contracts'
    
    id = Column(Integer, primary_key=True,nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    contract_type_id = Column(String, ForeignKey('contract_types.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    terms = Column(String, nullable=True)

    #relationships
    employee = relationship("Employee", back_populates="contracts")
    contract_type = relationship("ContractType", back_populates="employee_contracts")

    #utility methods
    def __repr__(self):
        return f"<EmployeeContract(id={self.id}, employee_id={self.employee_id}, contract_type_id='{self.contract_type_id}', start_date={self.start_date}, end_date={self.end_date})>"  