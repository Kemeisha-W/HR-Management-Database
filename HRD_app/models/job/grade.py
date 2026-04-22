from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class Grade(Base):
    __tablename__ = "grade"
    code = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    job = relationship("Job", back_populates="grade")

         #Utility Methods
    def __repr__(self):
        return f"<Grade(code='{self.code}', name='{self.name}')>"