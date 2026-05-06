# class EmployeeSupervisor(Base):
#     __tablename__ = "employee_supervisor"
#     id = Column(Integer,primary_key=True)
#     start_date = Column(Date)
#     end_date = Column(Date)
#     supervisor_id = Column(Integer, ForeignKey("Employee.id"))
#     supervisor_id = relationship("Employee", back_populates="EmployeeSupervisor")