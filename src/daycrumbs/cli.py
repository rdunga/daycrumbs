from datetime import datetime
import textwrap
import typer
from daycrumbs.activity import Activity
from daycrumbs.storage import Storage
from typing import Annotated

app = typer.Typer()

@app.command()
def add(notes: Annotated[list[str], typer.Argument()], 
        bucket: Annotated[str, typer.Option("--bucket", help="Optional bucket/category for the activity")] = None, 
        duration: Annotated[int, typer.Option("--duration", help="Duration of the activity in minutes")] = None):
    """
    Add a new activity to the daycrumbs.
    """
   # typer.echo("Adding a new activity...")
    notes = " ".join(notes)  # Join the list of notes into a single string
    activity = Activity(
        notes=notes,
        timestamp=datetime.now(),
        bucket=bucket,
        duration_mins=duration
    )
   # typer.echo(f"Activity added: {activity.notes}, timestamp: {activity.timestamp}, Bucket: {activity.bucket}, Duration: {activity.duration_mins} mins")

    storage = Storage()
    typer.echo(f"Storing activity in: {storage.app_data_dir}")
    storage.append_activity(activity)

@app.command()
def view(date: Annotated[str, typer.Argument(help="Date in YYYY-MM-DD format")] = None):
    """
    View activities for a specific date.
    """
    try:
        if date is None:
            date = str(datetime.now().date())

        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        typer.echo("Invalid date format. Please use YYYY-MM-DD.")
        raise typer.Exit(code=1)

    storage = Storage()
    activities = storage.get_activities(date_obj)
    
    if not activities:
        typer.echo(f"No activities found for {date_obj.strftime('%Y-%m-%d')}.")
        return

    typer.echo(f"Activities for {date}:")
    typer.echo("-" * 40)
    for activity in activities:
        timestamp = datetime.fromisoformat(activity['timestamp'])
        time_text = timestamp.strftime('%I:%M %p')
        
        wrapped_notes =  textwrap.wrap(activity['notes'], width=60)
        
        typer.echo(f"{time_text}  {wrapped_notes[0]}")
        for line in wrapped_notes[1:]:
            typer.echo(f"{' ' * 10}{line}") 

if __name__ == "__main__":
    app()