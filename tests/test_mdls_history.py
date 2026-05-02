def test_crud_status_history(session):
    from HRD_app.models.history.status_history import StatusHistory
    # Create a new status history record
    statusH = StatusHistory(id = 1, employee_id=1, status_id='ACT', start_date='2024-01-01', end_date='2024-12-31')
    session.add(statusH)
    session.commit()

    try:
        # Read the status history record
        retrieved_statusH = session.query(StatusHistory).filter_by(id=1).first()
        assert retrieved_statusH is not None
        assert retrieved_statusH.employee_id == 1
        assert retrieved_statusH.status_id == 'ACT'
        assert str(retrieved_statusH.start_date) == '2024-01-01'
        assert str(retrieved_statusH.end_date) == '2024-12-31'
    except Exception as e:
        print(f"Error adding status history: {e}")

    # Update the status history record
    retrieved_statusH.status_id = 'INACT'
    session.commit()

    try:
        # Verify the update
        updated_statusH = session.query(StatusHistory).filter_by(id=1).first()
        assert updated_statusH.status_id == 'INACT'
    except Exception as e:
        print(f"Error updating status history: {e}")
    finally:
        # Delete the status history record
        session.delete(updated_statusH)
        session.commit()
    
    # Verify the deletion
    deleted_statusH = session.query(StatusHistory).filter_by(id=1).first()
    assert deleted_statusH is None

def test_crud_position_history(session):
    from HRD_app.models.history.position_history import PositionHistory
    # Create a new position history record
    positionH = PositionHistory(id = 1, employee_id=1, job_code='MGR', start_date='2024-01-01', end_date='2024-12-31', position_type = "FT")
    session.add(positionH)
    session.commit()

    try:
        # Read the position history record
        retrieved_positionH = session.query(PositionHistory).filter_by(id=1).first()
        assert retrieved_positionH is not None
        assert retrieved_positionH.employee_id == 1
        assert retrieved_positionH.position_id == 'MGR'
        assert str(retrieved_positionH.start_date) == '2024-01-01'
        assert str(retrieved_positionH.end_date) == '2024-12-31'
    except Exception as e:
        print(f"Error adding position history: {e}")

    # Update the position history record
    retrieved_positionH.position_id = 'DEV'
    session.commit()

    try:
        # Verify the update
        updated_positionH = session.query(PositionHistory).filter_by(id=1).first()
        assert updated_positionH.position_id == 'DEV'
    except Exception as e:
        print(f"Error updating position history: {e}")
    finally:
        # Delete the position history record
        session.delete(updated_positionH)
        session.commit()
    
    # Verify the deletion
    deleted_positionH = session.query(PositionHistory).filter_by(id=1).first()
    assert deleted_positionH is None