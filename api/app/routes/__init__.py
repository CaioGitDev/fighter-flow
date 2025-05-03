from .auth_routes import auth_bp
from .user_routes import user_bp
from .team_routes import team_bp
from .fighter_routes import fighter_bp
from .fight_routes import fight_bp
from .fight_result_routes import fight_result_bp
from .country_routes import country_bp


# registar as rotas criadas 
def register_routes(app):
    app.register_blueprint(user_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(team_bp, url_prefix="/api")
    app.register_blueprint(fighter_bp, url_prefix="/api")
    app.register_blueprint(fight_bp, url_prefix="/api")
    app.register_blueprint(fight_result_bp, url_prefix="/api")
    app.register_blueprint(country_bp, url_prefix="/api")
