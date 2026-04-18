
def test_crud_company(session):
    from HRD_app.models.organization.company import Company
    company = Company(code = "COMPTest", name = "Test Company Ltd", location_id = 1)
    session.add(company)
    session.commit()
    try:
        retrieved_company = session.query(Company).first()
        assert retrieved_company is not None
        assert retrieved_company.name == "Test Company Ltd"
        assert retrieved_company.location_id == 1
    finally:
        session.delete(company)
        session.commit()

def  test_crud_division(session):
    from HRD_app.models.organization.division import Division
    division = Division(code = "DIVTest", name = "Division Name", company_code = "COMPTest")
    session.add(division)
    session.commit()

    try:
        retrieved_div = session.query(Division).first()
        assert retrieved_div is not None
        assert retrieved_div.name == "Division Name"
        assert retrieved_div.company_code == "COMPTest"
    finally:
        session.delete(division)
        session.commit()

def test_crud_department(session):
    from HRD_app.models.organization.department import Department
    dept = Department(code = "DEPTTest", name = "Department Name", division_code = "DIVTest")
    session.add(dept)
    session.commit()

    try:
        retrieved_dept = session.query(Department).first()
        assert retrieved_dept is not None
        assert retrieved_dept.name == "Department Name"
        assert retrieved_dept.division_code == "DIVTest"
    finally:
        session.delete(dept)
        session.commit()

def test_crud_location(session):
    from HRD_app.models.organization.location import Location
    location = Location(id = 1, name = "Location Name", address = "123 Test St")
    session.add(location)
    session.commit()

    try:
        retrieved_location = session.query(Location).first()
        assert retrieved_location is not None
        assert retrieved_location.name == "Location Name"
        assert retrieved_location.address == "123 Test St"
    finally:
        session.delete(location)
        session.commit()



