from platformdirs import user_data_dir
from pathlib import Path
from dataclasses import asdict
from datetime import date, datetime
import json

from daycrumbs.activity import Activity

class Storage:

    def __init__(self):
        self.app_data_dir = self._get_user_data_dir()


    def append_activity(self, activity):
        activity_dict = asdict(activity)
        json_string = json.dumps(activity_dict,
                                 default=lambda o: o.isoformat() if isinstance(o,datetime) else str(o),
                                 ensure_ascii=False)
        
        with open(self._get_file_path(activity), "a", encoding="utf-8") as f:
            f.write(json_string + "\n")

    def get_activities(self, date: datetime):
        """
        Returns a list of activities for a specific date.
        """ 
        if Path(self.app_data_dir / str(date.year) / str(f"{date.month:02d}") / f"{date.isoformat()}.jsonl").exists():
            jsonl_file_path = self.app_data_dir / str(date.year) / str(f"{date.month:02d}") / f"{date.isoformat()}.jsonl"
            with open(jsonl_file_path, "r", encoding="utf-8") as f:
                activities = [json.loads(line) for line in f]
            return activities
        else:
            return []

    def _get_user_data_dir(self):
        """
        Returns the directory path for storing activities.
        """
        path = Path(user_data_dir("daycrumbs"))
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    def _get_file_path(self, activity):
        """
        Returns the file path for storing activities for a specific date.
        """
        datetimestamp = activity.timestamp
        year_dir = self.app_data_dir / str(datetimestamp.year)
        month_dir = year_dir / str(f"{datetimestamp.month:02d}")
        month_dir.mkdir(parents=True, exist_ok=True)
        file_path = month_dir / f"{datetimestamp.date().isoformat()}.jsonl"
        return file_path
