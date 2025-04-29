from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flash_jwt_extended import JWTManager

# Initialize the database and JWT manager
db = SQLAlchemy()

# Initialize the JWT manager
jwt = JWTManager()

# Initialize the Flask application and configure it
# with the settings from the config module
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    # Register the database models and routes
    with app.app_context():
        from . import models, routes
        db.create_all()

    return app