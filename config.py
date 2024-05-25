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


class Config:
    """SQL Alchemy connection to PostgresSQL"""

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://data_admin:investigamer@localhost/ig_data_admin"
    )
    SECRET_KEY = "78f78214cd0360e847034d3bda9d117f"
    SQLALCHEMY_ECHO = False
    DEBUG = True
