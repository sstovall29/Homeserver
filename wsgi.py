from app import create_app
from app.extensions import socketio

app = create_app()

if app.config["USE_SOCKETIO"]:
    application = socketio
else:
    application = app