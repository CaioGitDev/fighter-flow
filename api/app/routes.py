from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from . import db
from .models import User

bp = Blueprint("main", __name__)

# Route to get the current user's information and check login
@bp.route("/login", methods=["POST"])
def login():
  data = request.get_json()
  username = data.get("username")
  password = data.get("password")

  user = User.query.filter_by(username=username).first()
  if user and user.check_password(password):
      token = create_access_token(identity={"id": user.id, "username": user.username})
      return jsonify({"access_token": token}), 200

  return jsonify({"error": "Credenciais inválidas"}), 401


# Route to get the current user's information
@bp.route("/user", methods=["GET"])
@jwt_required()
def get_user():
  current_user = get_jwt_identity()
  user = User.query.get(current_user["id"])
  if user:
      return jsonify({"username": user.username, "email": user.email}), 200

  return jsonify({"error": "Usuário não encontrado"}), 404


# Register the routes with the Flask app
def register_routes(app):
  app.register_blueprint(bp, url_prefix="/api")
  