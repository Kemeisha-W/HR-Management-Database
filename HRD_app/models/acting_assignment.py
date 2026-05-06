# class ActingAssignment(Base):
#     __tablename__ = "acting_assignments"
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     start_date = Column(Date)
#     end_date = Column(Date)
#     description = Column(String)
#     is_current = Column(Boolean,nullable=False)
#     employee = Column(Integer, ForeignKey("employee.id"))
#     employee = relationship("Employee", back_populates= "ActingAssignment")
#     job = Column(String, ForeignKey("job.code"))
#     job = relationship("Job", back_populates="ActingAssignment")