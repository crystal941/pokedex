from flask import Flask


def create_app():
    flask_app = Flask(__name__)

    with flask_app.app_context():
        # Register blueprints
        from home import home as home_blueprint
        flask_app.register_blueprint(home_blueprint.home_blueprint)

        from browse import browse as browse_blueprint
        flask_app.register_blueprint(browse_blueprint.browse_blueprint)

    return flask_app


if __name__ == "__main__":
    try:
        app = create_app()
        app.run(host='localhost', port=5000, threaded=False)
    except Exception as e:
        print(f"An error occurred: {e}")
