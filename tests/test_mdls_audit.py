def test_crud_auditlog(session):
    from HRD_app.models.audit.audit_log import AuditLog
    log = AuditLog(id = 1,user_id = 001,username = "User", password_hash = "test_password", email = "user1@gmail.com", role = "admin", is_active = True )
    session.add(log)
    session.commit

    try:
        retrieved = session.query(log).first()
        assert retrieved is not None
        assert retrieved.id == 1
        assert retrieved.user_id == 001
        assert retrieved.username == "User"
        assert retrieved.password_hash == "test_password"
        assert retrieved.email == "user1@gmail.com"
        assert retrieved.role == "admin"
        assert retrieved.is_active == True
    except Exception as e:
        print(f"Error during test add audit log: {e}")
    
    log.username = "Updated Username"
    session.commit
    updated_log = session.query(log).first()

    try:
        assert updated_log.username == "Updated Username"
    except Exception as e:
        print(f"Error during test updating audit log: {e}")
    finally:
        session.delete(log)
        session.commit
    
    #verify deletion
    deleted_log = session.query(log).filter_by(id = 1).first
    assert deleted_log is None

def test_crud_systemuser(session):
    from HRD_app.models.audit.system_user import SystemUser
    user = SystemUser(id = 1,employee_id = 001,username = "User", password_hash = "test_password", email = "user1@gmail.com", role = "admin", is_active = True )
    session.add(user)
    session.commit

    try:
        retrieved = session.query(user).first()
        assert retrieved is not None
        assert retrieved.id == 1
        assert retrieved.employee_id == 001
        assert retrieved.username == "User"
        assert retrieved.password_hash == "test_password"
        assert retrieved.email == "user1@gmail.com"
        assert retrieved.role == "admin"
        assert retrieved.is_active == True
    except Exception as e:
        print(f"Error during test add system user: {e}")

    user.email = "update@gmail.com"
    session.commit

    update_user =  session.query(user).first
    try:
        assert update_user == "update@gmail.com"
    except Exception as e:
        print(f"Error during update test : {e}")
    finally:
        session.delete
        session.commit

    #verify deletion
    del_user = session.query(user).filter_by(id = 1).first
    assert del_user is None

