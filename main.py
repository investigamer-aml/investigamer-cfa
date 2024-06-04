"""
This module is the entry point for a Flask application created with the `create_app` function from the 'app' package.

It configures the application based on the environment and runs the server.
"""
import os
from app import create_app

# Environment detection and mapping to configuration class
config_map = {
    "development": "DevelopmentConfig",
    "production": "ProductionConfig",
    "testing": "TestingConfig"
}

env = os.getenv("FLASK_ENV", "development")
config_class = config_map.get(env, "Config")

# Create app using the factory, passing in the configuration object from the map
app = create_app(config_class)

if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG", False))