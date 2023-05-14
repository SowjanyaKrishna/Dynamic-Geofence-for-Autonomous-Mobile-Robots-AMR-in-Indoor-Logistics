from app import create_app, db
from app.models import User, SpeedRange, SpeedRangeSchema


app = create_app()


@app.shell_context_processor  # allows you to get the flask app context in the cli by running flask shell, which is great for debugging
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "SpeedRange": SpeedRange,
        "SpeedRangeSchema": SpeedRangeSchema,
    }
