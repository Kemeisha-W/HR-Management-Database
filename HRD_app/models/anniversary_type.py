from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from HRD_app.database import Base

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

    #relationships
    anniversaries = relationship("Anniversary", back_populates="anniversary_type")

    #utility method
    def __repr__(self):
        return f"AnniversaryType(id={self.id}, name='{self.name}', description='{self.description}', created_date={self.created_date}, update_date={self.update_date}, anniversary_date={self.anniversary_date}, created_by='{self.created_by}', updated_by='{self.updated_by}')"   