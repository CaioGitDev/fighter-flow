from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from ..models import Fighter
from .. import db

fighter_bp = Blueprint("fighter", __name__)


# ===== Helpers =====

def serialize_fighter(fighter):
    return {
        "id": fighter.id,
        "first_name": fighter.first_name,
        "last_name": fighter.last_name,
        "nickname": fighter.nickname,
        "weight": fighter.weight,
        "team_id": fighter.team_id,
        "wins": fighter.wins,
        "losses": fighter.losses,
        "draws": fighter.draws,
        "created_at": fighter.created_at,
        "updated_at": fighter.updated_at
    }


def get_fighter_by_id(fighter_id):
    return db.session.query(Fighter).filter_by(id=fighter_id).first()


def validate_fighter_data(data):
    required_fields = ["first_name", "last_name", "nickname", "weight", "team_id"]
    missing_fields = [field for field in required_fields if not data.get(field)]
    if missing_fields:
        return f"Missing required fields: {', '.join(missing_fields)}"
    return None


# ===== Routes =====

@fighter_bp.route("/fighters", methods=["GET"])
@jwt_required()
def list_fighters():
    fighters = db.session.query(Fighter).all()
    return jsonify({"data": [serialize_fighter(f) for f in fighters]}), 200


@fighter_bp.route("/fighter/<int:fighter_id>", methods=["GET"])
@jwt_required()
def get_fighter(fighter_id):
    fighter = get_fighter_by_id(fighter_id)
    if not fighter:
        return jsonify({"error": "Fighter not found"}), 404
    return jsonify({"data": serialize_fighter(fighter)}), 200


@fighter_bp.route("/fighter", methods=["POST"])
@jwt_required()
def create_fighter():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    validation_error = validate_fighter_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    existing_fighter = db.session.query(Fighter).filter_by(
        first_name=data["first_name"],
        last_name=data["last_name"],
        nickname=data["nickname"]
    ).first()

    if existing_fighter:
        return jsonify({"error": "Fighter already exists"}), 409

    new_fighter = Fighter(
        first_name=data["first_name"],
        last_name=data["last_name"],
        nickname=data["nickname"],
        weight=data["weight"],
        team_id=data["team_id"],
        wins=data.get("wins", 0),
        losses=data.get("losses", 0),
        draws=data.get("draws", 0)
    )

    db.session.add(new_fighter)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"data": serialize_fighter(new_fighter)}), 201


@fighter_bp.route("/fighter/<int:fighter_id>", methods=["PUT"])
@jwt_required()
def update_fighter(fighter_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body is required"}), 400

    validation_error = validate_fighter_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    fighter = get_fighter_by_id(fighter_id)
    if not fighter:
        return jsonify({"error": "Fighter not found"}), 404

    fighter.first_name = data["first_name"]
    fighter.last_name = data["last_name"]
    fighter.nickname = data["nickname"]
    fighter.weight = data["weight"]
    fighter.team_id = data["team_id"]
    fighter.wins = data.get("wins", fighter.wins)
    fighter.losses = data.get("losses", fighter.losses)
    fighter.draws = data.get("draws", fighter.draws)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"data": serialize_fighter(fighter)}), 200


@fighter_bp.route("/fighter/<int:fighter_id>", methods=["DELETE"])
@jwt_required()
def delete_fighter(fighter_id):
    fighter = get_fighter_by_id(fighter_id)
    if not fighter:
        return jsonify({"error": "Fighter not found"}), 404

    try:
        db.session.delete(fighter)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({"data": "Fighter removed"}), 200
