from flask import Flask


def create_app():
    app = Flask(__name__)

    # import routes
    from .routes.main_route import main_bp

    # register routes
    app.register_blueprint(main_bp)

    return app
