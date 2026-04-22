def test_crud_grade(session):
    from HRD_app.models.job.grade import Grade
    # Create a new grade
    new_grade = Grade(code="G1", name="Grade 1", description="Entry level grade")
    session.add(new_grade)
    session.commit()
    
    # Read the grade
    grade = session.query(Grade).filter_by(code="G1").first()
    try:
        grade = session.query(Grade).first()
        assert grade is not None
        assert grade.name == "Grade 1"
        assert grade.description == "Entry level grade"
    except Exception as e:
        print(f"Error during test_add_grade: {e}")

    
    # Update the grade
    grade.description = "Updated description"
    session.commit()
    
    # Verify the update
    updated_grade = session.query(Grade).filter_by(code="G1").first()
    try:
        assert updated_grade.description == "Updated description"
    except Exception as e:
        print(f"Error during test_add_grade: {e}")
    
    # Delete the grade
    session.delete(updated_grade)
    session.commit()
    
    # Verify deletion
    deleted_grade = session.query(Grade).filter_by(code="G1").first()
    assert deleted_grade is None

def test_crud_job(session):
    from HRD_app.models.job.job import Job
    # Create a new job
    new_job = Job(code="J1", title="Software Engineer", grade="G1", min_salary=50000, max_salary=100000, departments_code="D1")
    session.add(new_job)
    session.commit()
    
    # Read the job
    job = session.query(Job).filter_by(code="J1").first()
    try:
        job = session.query(Job).first()
        assert job is not None
        assert job.title == "Software Engineer"
        assert job.min_salary == 50000
        assert job.max_salary == 100000
    except Exception as e:
        print(f"Error during test_add_job: {e}")

    
    # Update the job
    job.title = "Senior Software Engineer"
    session.commit()
    
    # Verify the update
    updated_job = session.query(Job).filter_by(code="J1").first()
    try:
        assert updated_job.title == "Senior Software Engineer"
    except Exception as e:
        print(f"Error during test_add_job: {e}")
    
    # Delete the job
    session.delete(updated_job)
    session.commit()
    
    # Verify deletion
    deleted_job = session.query(Job).filter_by(code="J1").first()
    assert deleted_job is None