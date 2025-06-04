from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import timedelta
from ..models import User

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
      token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
      return jsonify({"access_token": token}), 200

  return jsonify({"error": "Credenciais inválidas"}), 401