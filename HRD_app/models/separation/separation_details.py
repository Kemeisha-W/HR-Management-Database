# TODO
# class SeparationDetail(Base):
#     __tablename__ = "separation_details"
#     id = Column(Integer,primary_key=True)
#     separation_date = Column(Date)
#     notes = Column(String)
#     rehire_eligibility = Column(Boolean)
#     employee_id = Column(Integer, ForeignKey("Employee.id"))
#     employee_id = relationship("Employee", back_populates="SeparationDetail")
#     reason_id = Column(Integer, ForeignKey("SeparationReason.id"))
#     reason_id = relationship("SeparationReason", back_populates="SeparationDetail")