"""
Configuration settings for the Flask application.

This configuration class sets up essential parameters for the Flask application,
including database connections, debugging options, and security settings.

Attributes:
    SQLALCHEMY_DATABASE_URI (str): Database connection URI for SQLAlchemy. This URI specifies
                                   the username, password, server location, and database name
                                   used to connect to a PostgreSQL database.
    SECRET_KEY (str): A secret key used by Flask for securely signing the session cookie.
                      It is crucial for security and should be kept secret in production.
    SQLALCHEMY_ECHO (bool): When set to True, SQLAlchemy will log all the statements issued to stderr
                            which can be useful for debugging.
    DEBUG (bool): Enables or disables debug mode. When True, provides detailed error logs and
                  auto-reloads the server on code changes.
"""
import os

from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env into the environment


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URI = os.getenv("DATABASE_URI")
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = False
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = os.getenv("TEST_DATABASE_URI")
