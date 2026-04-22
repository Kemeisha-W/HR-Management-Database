from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class ContractType(Base):
    __tablename__ = "contract_type"
    id = Column(String,primary_key=True)
    name = Column(String)
    duration = Column(String)
    contract = relationship("Contract", back_populates="ContractType")

     #Utility Methods
    def __repr__(self):
        return f"<ContractType(id='{self.id}', name='{self.name}')>"
