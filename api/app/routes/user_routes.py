from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/user", methods=["GET"])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if user:
        return jsonify({"data": {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "last_login": user.last_login,
        "created_at": user.created_at
    }}), 200

    return jsonify({"error": "Usuário não encontrado"}), 404