from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """
    Creates and configures an instance of the Flask application.

    Sets up the configuration, initializes the database, and registers the login manager.
    Routes are imported and the database tables are created within the application context.
    This setup pattern follows the application factory pattern recommended by Flask for larger applications.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    login_manager.init_app(app)
    # toolbar = DebugToolbarExtension(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()

    return app
