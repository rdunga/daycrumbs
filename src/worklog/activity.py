from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class Activity:
    """
    Represents an activity performed by a user.
    """
    notes: str
    timestamp: datetime
    bucket: str | None = None  # Optional bucket/category for the activity
    duration_mins: int | None = None  # Duration in mins, optional

