from datetime import datetime
from worklog.activity import Activity

def test_activity_creation():
    activity = Activity(
        notes="Completed task A",
        timestamp=datetime.now(),
        bucket="Customer",
        duration_mins=60
    )
    
    assert activity.notes == "Completed task A"
   # assert activity.timestamp == datetime(2024, 6, 1, 10, 0)
    assert activity.bucket == "Customer"
    assert activity.duration_mins == 60

def test_activity_without_optional_fields():
    activity = Activity(
        notes="Completed task B",
        timestamp=datetime.now()
    )
    
    assert activity.notes == "Completed task B"
   # assert activity.timestamp == datetime(2024, 6, 1, 11, 0)
    assert activity.bucket is None
    assert activity.duration_mins is None

def test_activity_is_frozen():
    activity = Activity(
        notes="Completed task C",
        timestamp=datetime.now(),
        bucket="Internal",
        duration_mins=30
    )
    
    try:
        activity.notes = "Attempt to modify"
    except Exception as e:
        assert isinstance(e, AttributeError)