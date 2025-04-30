from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from . import db
from .models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
  data = request.get_json()
  email = data.get("email")
  password = data.get("password")
  
  if not email or not password:
      return jsonify({"error": "Email e senha são obrigatórios"}), 400

  user = User.query.filter_by(email=email).first()
  if user and user.check_password(password):
      token = create_access_token(identity=str(user.id))
      return jsonify({"access_token": token}), 200

  return jsonify({"error": "Credenciais inválidas"}), 401


# Route to get the current user's information
@auth_bp.route("/user", methods=["GET"])
@jwt_required()
def get_user():
  user_id = get_jwt_identity()
  user = User.query.get(int(user_id))
  if user:
      return jsonify({"username": user.username, "email": user.email}), 200

  return jsonify({"error": "Usuário não encontrado"}), 404


# Register the routes with the Flask app
def register_routes(app):
  app.register_blueprint(bp, url_prefix="/api")
  