""" Init for the app
"""
import os

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class="Config"):
    """
    Creates and configures an instance of the Flask application.
    """
    app = Flask(__name__)
    CORS(app)
    config_module = __import__("config", fromlist=[config_class])
    app.config.from_object(getattr(config_module, config_class))

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Consider using migrations in production

        # Register your blueprints
        from .use_case import \
            use_case_bp  # Make sure to import correctly based on your project structure

        app.register_blueprint(use_case_bp)  # You can specify a URL prefix if desired

    return app
