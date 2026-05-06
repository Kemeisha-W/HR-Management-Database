from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class SeparationReason(Base):
    __tablename__ = 'separation_reasons'

    id = Column(Integer, primary_key = True)
    description = Column(String)
    
    #relationship
    sep_details = relationship("SeparationDetail", back_populates="SeparationReason")

    #Utility Method
    def __repr__(self):
        return f"<SeparationReason(id={self.id}, description='{self.description}')>"