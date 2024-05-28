"""
This module is the entry point for a Flask application created with the `create_app` function from the 'app' package.

It configures the application based on the environment and runs the server.
"""
import os

from app import create_app

# Environment detection
env = os.getenv("FLASK_ENV", "development")

# Create app using the factory, passing in the environment to select the configuration
app = create_app(env)

if __name__ == "__main__":
    # Run the application
    app.run(debug=app.config["DEBUG"])
