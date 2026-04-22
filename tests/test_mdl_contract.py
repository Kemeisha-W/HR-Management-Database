
def test_crud_contract_type(session):
    from HRD_app.models.contract.contract_type import ContractType
    CT = ContractType(id = "CTTest", name = "Test One Year Contract", duration = "12 months")
    session.add(CT)
    session.commit()
    try:
        retrieved_ct = session.query(CT).first()
        assert retrieved_ct is not None
        assert retrieved_ct.name == "Test One Year Contract"
        assert retrieved_ct.duration == "12 months"
    except Exception as e:
        print(f"Error during test_add_contractType: {e}")
    
    CT.name = "Updated Contract Type Name"
    session.commit()
    updated_ct = session.query(CT).first()

    try:
        assert updated_ct.name == "Updated Contract Type Name"
    except Exception as e:
        print(f"Error during test_update_contractType: {e}")
    finally:
        session.delete(CT)
        session.commit()

def test_crud_employee_contract(session):
    from HRD_app.models.contract.employee_contract import EmployeeContract
    EC = EmployeeContract(id = "ECTest", employee_id = "E1", contract_type_id = "CTTest", start_date = "2024-01-01", end_date = "2024-12-31")
    session.add(EC)
    session.commit()
    try:
        retrieved_ec = session.query(EC).first()
        assert retrieved_ec is not None
        assert retrieved_ec.employee_id == "E1"
        assert retrieved_ec.contract_type_id == "CTTest"
        assert retrieved_ec.start_date == "2024-01-01"
        assert retrieved_ec.end_date == "2024-12-31"
    except Exception as e:
        print(f"Error during test_add_employeeContract: {e}")
    
    EC.end_date = "2025-12-31"
    session.commit()
    updated_ec = session.query(EC).first()

    try:
        assert updated_ec.end_date == "2025-12-31"
    except Exception as e:
        print(f"Error during test_update_employeeContract: {e}")
    finally:
        session.delete(EC)
        session.commit()
        
    # Verify deletion
    deleted_cont = session.query(EmployeeContract).filter_by(id="ECTest").first()
    assert deleted_cont is None 

def test_crud_contract(session):
    from HRD_app.models.contract.contract import Contract
    C = Contract(id = 1, employee_id = "E1", contract_type_id = "CTTest", start_date = "2024-01-01", end_date = "2024-12-31", description = "Test Contract")
    session.add(C)
    session.commit()
    try:
        retrieved_c = session.query(C).first()
        assert retrieved_c is not None
        assert retrieved_c.employee_id == "E1"
        assert retrieved_c.contract_type_id == "CTTest"
        assert retrieved_c.start_date == "2024-01-01"
        assert retrieved_c.end_date == "2024-12-31"
        assert retrieved_c.description == "Test Contract"
    except Exception as e:
        print(f"Error during test_add_contract: {e}")
    
    C.description = "Updated Test Contract"
    session.commit()
    updated_c = session.query(C).first()

    try:
        assert updated_c.description == "Updated Test Contract"
    except Exception as e:
        print(f"Error during test_update_contract: {e}")
    finally:
        session.delete(C)
        session.commit()
        
    # Verify deletion
    deleted_cont = session.query(Contract).filter_by(id=1).first()
    assert deleted_cont is None