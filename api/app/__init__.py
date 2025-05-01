from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from  flask_migrate import Migrate

# Inicializa os objetos antes de qualquer import que dependa deles
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)  # Ativa CORS para todas as rotas

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # Importa o blueprint depois de inicializar o app
    from app.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api")

    with app.app_context():
        from . import models
        db.create_all()

    return app
