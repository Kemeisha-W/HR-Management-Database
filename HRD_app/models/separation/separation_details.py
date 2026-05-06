from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class SeparationDetail(Base):
    __tablename__ = "separation_details"
    id = Column(Integer,primary_key=True)
    separation_date = Column(Date)
    notes = Column(String)
    rehire_eligibility = Column(Boolean)
    employee_id = Column(Integer, ForeignKey("Employee.id"))
    reason_id = Column(Integer, ForeignKey("SeparationReason.id"))

    #Relationships
    employee_id = relationship("Employee", back_populates="SeparationDetail")
    reason_id = relationship("SeparationReason", back_populates="SeparationDetail")

    #Utility Methods
    def __repr__(self):
        return f"<SeparationDetail(id={self.id}, separation_date={self.separation_date}, notes='{self.notes}', rehire_eligibility={self.rehire_eligibility})>"