
from datetime import datetime
import json

from daycrumbs.storage import Storage
from daycrumbs.activity import Activity

def test_storage_initialization():
    storage = Storage()
    assert storage.app_data_dir is not None


def test_append_activity_creates_file(tmp_path):
    storage = Storage()
    storage.app_data_dir = tmp_path  # Override the app_data_dir for testing

    activity = Activity(
        notes="Test activity",
        timestamp=datetime(2024, 6, 1, 10, 0),
        bucket="TestBucket",
        duration_mins=30
    )

    storage.append_activity(activity)

    expected_file_path = tmp_path / "2024" / "06" / "2024-06-01.jsonl"
    assert expected_file_path.exists()

    with open(expected_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        assert len(lines) == 1
        stored_activity = json.loads(lines[0])
        assert stored_activity["notes"] == "Test activity"
        assert stored_activity["bucket"] == "TestBucket"
        assert stored_activity["duration_mins"] == 30