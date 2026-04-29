from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from HRD_app.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("system_user.id"))
    timestamp = Column(Date)
    tablename = Column(String)
    operation_type = Column(String)
    changed_by = Column(String)
    old_value = Column(String)
    new_value = Column(String)
    details = Column(String)

    #relationships
    user_id = relationship("SystemUser",back_populates="AuditLog")

    #Utility Methods
    def __repr__(self):
        return f"<AuditLog(id='{self.id}',user id = '{self.user_id}',Table Name = '{self.tablename},'timestamp = '{self.timestamp}', Operation Type = '{self.operation_type}', Changed By = '{self.changed_by}', Old Value = '{self.old_value}', New Value = '{self.new_value}', Details = '{self.details}')"
    