from flask import Flask
from .routes import register_routes
from .extensions import socketio
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_routes(app)

    if app.config["USE_SOCKETIO"]:
        socketio.init_app(
            app,
            async_mode=app.config["SOCKETIO_ASYNC_MODE"]
        )

        # Import handlers ONLY if enabled
        from . import sockets
    
    @app.context_processor
    def inject_config():
        return {
        "USE_SOCKETIO": app.config["USE_SOCKETIO"],
        "APP_NAME": app.config.get("APP_NAME", "My App")
    }
      
    return app