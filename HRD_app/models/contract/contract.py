from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class Contract(Base):
    __tablename__ = "contracts"
    id = Column(Integer,primary_key=True)
    probation_end_date = Column(Date)
    start_date = Column(Date)
    end_date = Column(Date)
    description = Column(String)
    contract_type_id = Column(String, ForeignKey("ContractType.id"))
    employee_id = Column(Integer, ForeignKey("employee.id"))

    #relationships
    contract_type_id = relationship("ContractType", back_populates="Contract")
    employee_id = relationship("Employee", back_populates="Contract")

    #Utility Methods
    def __repr__(self):
        return f"<Contract(id='{self.id}', employee_id='{self.employee_id}', contract_type_id='{self.contract_type_id}')>"