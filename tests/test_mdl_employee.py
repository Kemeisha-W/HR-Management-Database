def test_crud_employee(session):
    from HRD_app.models.employee.employee import Employee
    E = Employee(
        id = "E1", 
        name = "Test Employee", 
        email = "test.employee@example.com", 
        hiredate = "2024-01-01", 
        birthdate = "1990-01-01", 
        phone_number = 1234567890
        location = "L1",
        job = "J1",
        status_id = "ESTest",
        emp_type = "ETTest",
        anniversary = "AT1",
        contract = "C1"
    )
    
    session.add(E)
    session.commit()
    try:
        assert E.id == "E1"
        assert E.name == "Test Employee"
        assert E.email == "test.employee@example.com"
        assert E.hiredate == "2024-01-01"
        assert E.birthdate == "1990-01-01"
        assert E.phone_number == 1234567890
        assert E.location == "L1"
        assert E.job == "J1"
        assert E.status_id == "ESTest"
        assert E.emp_type == "ETTest"
        assert E.anniversary == "AT1"
        assert E.contract == "C1"
    except Exception as e:
        print(f"Error Occurred: {e}")
    

    session.delete(E)
    session.commit()
    
def test_crud_employee_type(session):
    from HRD_app.models.employee.employee_type import EmployeeType
    ET = EmployeeType(id = "ETTest", name = "Test Employee Type")
    session.add(ET)
    session.commit()
    assert ET.id == "ETTest"
    assert ET.name == "Test Employee Type"
    session.delete(ET)

def test_crud_employee_status(session):
    from HRD_app.models.employee.employee_status import EmployeeStatus
    ES = EmployeeStatus(id = "ESTest", name = "Test Employee Status")
    session.add(ES)
    session.commit()
    assert ES.id == "ESTest"
    assert ES.name == "Test Employee Status"
    session.delete(ES)
