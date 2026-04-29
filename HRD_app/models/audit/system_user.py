from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class SystemUser(Base):
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey)
    username = Column(String)
    password_hash = Column(String)
    email = Column(String)
    role = Column(String)
    is_active = Column(Boolean)

    #relationships
    
    employee_id = relationship("Employee", back_populates="SystemUser")

    #Utility Method
    def __repr__(self):
        return f"ID = '{self.id}', Username = '{self.username}', Password = '{self.password_hash}, Email = '{self.email}', role = '{self.role}', is_active = '{self.is_active}'"