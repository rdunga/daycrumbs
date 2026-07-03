from datetime import datetime
import typer
from worklog.activity import Activity
from typing import Annotated

app = typer.Typer()

@app.command()
def add(notes: Annotated[str, typer.Argument()], 
        bucket: Annotated[str, typer.Option("--bucket", help="Optional bucket/category for the activity")] = None, 
        duration: Annotated[int, typer.Option("--duration", help="Duration of the activity in minutes")] = None):
    """
    Add a new activity to the worklog.
    """
    typer.echo("Adding a new activity...")
    activity = Activity(
        notes=notes,
        timestamp=datetime.now(),
        bucket=bucket,
        duration_mins=duration
    )
    typer.echo(f"Activity added: {activity.notes}, timestamp: {activity.timestamp}, Bucket: {activity.bucket}, Duration: {activity.duration_mins} mins")

if __name__ == "__main__":
    app()