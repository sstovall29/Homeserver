from .extensions import socketio
from datetime import datetime

@socketio.on("connect")
def handle_connect():
    print("Client connected")

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")

@socketio.on("hello")
def hello():
    print("Hello Sever")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    socketio.emit("Hello Client", {"time sent:": timestamp})

