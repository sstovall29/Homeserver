from app import create_app
from app.extensions import socketio

app = create_app()

if __name__ == "__main__":
    if app.config["USE_SOCKETIO"]:
        socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
        # socketio.run(
        #     app,
        #     host="0.0.0.0",
        #     port=5000,
        #     debug=True,
        #     allow_unsafe_werkzeug=True
        # )
    else:
        # To run locally
        # app.run(debug=True)

        # To push to public port 5000
        app.run(
            host="0.0.0.0",
            port=5000,
            debug=True
        )