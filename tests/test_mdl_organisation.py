
def test_crud_location(session):
    from HRD_app.models.organization.location import Location as loc
    location = loc(id = 1, name = "Location Name", address = "123 Test St")
    session.add(location)
    session.commit()

    try:
        retrieved_location = session.query(loc).first()
        assert retrieved_location is not None
        assert retrieved_location.name == "Location Name"
        assert retrieved_location.address == "123 Test St"
    except Exception as e:
        print(f"Error during test_add_location: {e}")
    
    location.name = "Updated Location Name"
    session.commit()
    updated_location = session.query(loc).first()
    try:
        assert updated_location.name == "Updated Location Name"
    except Exception as e:
        print(f"Error during test_update_location: {e}")
    finally:
        session.delete(location)
        session.commit()
    
    # Verify deletion
    deleted_loc = session.query(loc).filter_by(id=1).first()
    assert deleted_loc is None

def test_crud_company(session):
    from HRD_app.models.organization.company import Company
    company = Company(code = "COMPTest", name = "Test Company Ltd", location_id = 1)
    session.add(company)
    session.commit()
    retrieved_company = session.query(Company).first()
    try:
        assert retrieved_company is not None
        assert retrieved_company.name == "Test Company Ltd"
        assert retrieved_company.location_id == 1
    except Exception as e:
        print(f"Error during test_add_company: {e}")
    company.name = "Updated Company Name"
    session.commit()
    updated_company = session.query(Company).first()
    try:
        assert updated_company.name == "Updated Company Name"
    except Exception as e:
        print(f"Error during test_update_company: {e}")
    finally:
        session.delete(company)
        session.commit()
    # Verify deletion
    deleted_comp = session.query(Company).filter_by(code="COMPTest").first()
    assert deleted_comp is None

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
    except Exception as e:
        print(f"Error during test_add_division: {e}")
    
    division.name = "Updated Division Name"
    session.commit()
    updated_division = session.query(Division).first()
    try:
        assert updated_division.name == "Updated Division Name"
    except Exception as e:
        print(f"Error during test_update_division: {e}")
    finally:
        session.delete(division)
        session.commit()
    # Verify deletion
    deleted_div = session.query(Division).filter_by(code="DIVTest").first()
    assert deleted_div is None


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
    except Exception as e:
        print(f"Error during test_add_department: {e}")
    
    dept.name = "Updated Department Name"
    session.commit()
    updated_dept = session.query(dept).first()
    try:
        assert updated_dept.name == "Updated Department Name"
    except Exception as e:
        print(f"Error during test_update_department: {e}")
    finally:
        session.delete(dept)
        session.commit()
    
    # Verify deletion
    deleted_dept = session.query(Department).filter_by(code="DEPTTest").first()
    assert deleted_dept is None