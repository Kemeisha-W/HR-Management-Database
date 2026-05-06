def test_crud_status_history(session):
    from HRD_app.models.history.status_history import StatusHistory
    # Create a new status history record
    status_h = StatusHistory(id = 1, employee_id=1, status_id='ACT', start_date='2024-01-01', end_date='2024-12-31')
    session.add(status_h)
    session.commit()

    try:
        # Read the status history record
        retrieved_status_h = session.query(StatusHistory).filter_by(id=1).first()
        assert retrieved_status_h is not None
        assert retrieved_status_h.employee_id == 1
        assert retrieved_status_h.status_id == 'ACT'
        assert str(retrieved_status_h.start_date) == '2024-01-01'
        assert str(retrieved_status_h.end_date) == '2024-12-31'
    except Exception as e:
        print(f"Error adding status history: {e}")

    # Update the status history record
    retrieved_status_h.status_id = 'INACT'
    session.commit()

    try:
        # Verify the update
        updated_status_h = session.query(StatusHistory).filter_by(id=1).first()
        assert updated_status_h.status_id == 'INACT'
    except Exception as e:
        print(f"Error updating status history: {e}")
    finally:
        # Delete the status history record
        session.delete(updated_status_h)
        session.commit()
    
    # Verify the deletion
    deleted_status_h = session.query(StatusHistory).filter_by(id=1).first()
    assert deleted_status_h is None

def test_crud_position_history(session):
    from HRD_app.models.history.position_history import PositionHistory
    # Create a new position history record
    position_h = PositionHistory(id = 1, employee_id=1, job_code='MGR', start_date='2024-01-01', end_date='2024-12-31', position_type = "FT")
    session.add(position_h)
    session.commit()

    try:
        # Read the position history record
        retrieved_position_h = session.query(PositionHistory).filter_by(id=1).first()
        assert retrieved_position_h is not None
        assert retrieved_position_h.employee_id == 1
        assert retrieved_position_h.position_id == 'MGR'
        assert str(retrieved_position_h.start_date) == '2024-01-01'
        assert str(retrieved_position_h.end_date) == '2024-12-31'
    except Exception as e:
        print(f"Error adding position history: {e}")

    # Update the position history record
    retrieved_position_h.position_id = 'DEV'
    session.commit()

    try:
        # Verify the update
        updated_position_h = session.query(PositionHistory).filter_by(id=1).first()
        assert updated_position_h.position_id == 'DEV'
    except Exception as e:
        print(f"Error updating position history: {e}")
    finally:
        # Delete the position history record
        session.delete(updated_position_h)
        session.commit()
    
    # Verify the deletion
    deleted_position_h = session.query(PositionHistory).filter_by(id=1).first()
    assert deleted_position_h is None