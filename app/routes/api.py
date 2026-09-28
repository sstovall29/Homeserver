from flask import Blueprint, jsonify, current_app
from datetime import datetime
import time
import socket

api_bp = Blueprint("api", __name__, url_prefix="/api")

# Track when app started
START_TIME = time.time()

@api_bp.route("/status")
def status():
    uptime_seconds = int(time.time() - START_TIME)

    return jsonify({
        "status": "ok",
        "app_name": current_app.config.get("APP_NAME"),
        "socketio_enabled": current_app.config.get("USE_SOCKETIO"),
        "uptime_seconds": uptime_seconds,
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hostname": socket.gethostname()
    })