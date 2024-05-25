"""
This module is the entry point for a Flask application created with the `create_app` function from the 'app' package.

It configures the application and runs the server with debugging features turned on based on the application's configuration settings.
"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the application with debug mode based on the configuration
    app.run(debug=app.config["DEBUG"])
