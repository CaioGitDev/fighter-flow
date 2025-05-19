from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Fighter
from .. import db

fighter_bp = Blueprint("fighter", __name__)

@fighter_bp.route("/fighters", methods=["GET"])
@jwt_required()
def get_fighters():
    # List all fighters in the database
    results = db.session.query(Fighter).all()
    # Return a list of fighters with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": [
    {
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
    } for fighter in results    
    ]}), 200
  
@fighter_bp.route("/fighter/<int:fighter_id>", methods=["GET"])
@jwt_required()
def get_fighter(fighter_id):
    # List a specific fighter from the database by id
    fighter = db.session.query(Fighter).filter_by(id=fighter_id).first()
    # If the fighter does not exist, return a 404 error
    if not fighter:
        return jsonify({"error": "Fighter not found"}), 404
    
    # Return a fighter with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": {
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
    }}), 200
  
@fighter_bp.route("/fighter", methods=["POST"])
@jwt_required()
def create_fighter():
    # Create a new fighter in the database
    # The data should be sent in the request body in JSON format
    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    # The data should include: first name, last name, nickname, weight, team id, wins, losses, draws, active status
    first_name = body.get("first_name")
    last_name = body.get("last_name")
    nickname = body.get("nickname")
    weight = body.get("weight")
    team_id = body.get("team_id")
    wins = body.get("wins")
    losses = body.get("losses")
    draws = body.get("draws")
    
    # If the fighter already exists, return a 409 error
    
    existing_fighter = db.session.query(Fighter).filter_by(
        first_name=first_name,
        last_name=last_name,
        nickname=nickname,
    ).first()
    if existing_fighter:
        return jsonify({"error": "Fighter already exists"}), 409
    # If the data is incorrect, return a 400 error
    if not first_name or not last_name or not nickname or not weight or not team_id:
        return jsonify({"error": "All fields are required"}), 400
    # If everything is ok, create the fighter 
    new_fighter = Fighter(
        first_name=first_name,
        last_name=last_name,
        nickname=nickname,
        weight=weight,
        team_id=team_id,
        wins=wins,
        losses=losses,
        draws=draws
    )
    db.session.add(new_fighter)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    # Return the created fighter with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": {
        "id": new_fighter.id,
        "first_name": new_fighter.first_name,
        "last_name": new_fighter.last_name,
        "nickname": new_fighter.nickname,
        "weight": new_fighter.weight,
        "team_id": new_fighter.team_id,
        "wins": new_fighter.wins,
        "losses": new_fighter.losses,
        "draws": new_fighter.draws,
        "created_at": new_fighter.created_at,
        "updated_at": new_fighter.updated_at
    }}), 201
  
@fighter_bp.route("/fighter/<int:fighter_id>", methods=["PUT"])
@jwt_required()
def update_fighter(fighter_id):
    # Update an existing fighter in the database
    # The data should be sent in the request body in JSON format
    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    # The data should include: first name, last name, nickname, weight, team id, wins, losses, draws, active status
    first_name = body.get("first_name")
    last_name = body.get("last_name")
    nickname = body.get("nickname")
    weight = body.get("weight")
    team_id = body.get("team_id")
    wins = body.get("wins")
    losses = body.get("losses")
    draws = body.get("draws")
    # If the fighter does not exist, return a 404 error
    fighter = db.session.query(Fighter).filter_by(id=fighter_id).first()
    if not fighter:
        return jsonify({"error": "Fighter not found"}), 404
    # If the data is incorrect, return a 400 error
    if not first_name or not last_name or not nickname or not weight or not team_id:
        return jsonify({"error": "All fields are required"}), 400
    # If everything is ok, update the fighter 
    try:
        fighter.first_name = first_name
        fighter.last_name = last_name
        fighter.nickname = nickname
        fighter.weight = weight
        fighter.team_id = team_id
        fighter.wins = wins
        fighter.losses = losses
        fighter.draws = draws
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    # Return the updated fighter with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": {
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
    }}), 200
  
@fighter_bp.route("/fighter/<int:fighter_id>", methods=["DELETE"])
@jwt_required()
def delete_fighter(fighter_id):
    # Delete a fighter from the database by id
    # If the fighter does not exist, return a 404 error
    fighter = db.session.query(Fighter).filter_by(id=fighter_id).first()
    if not fighter:
        return jsonify({"error": "Fighter not found"}), 404
    # If everything is ok, delete the fighter 
    try:
        db.session.delete(fighter)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    # Return a success message

    return jsonify({"data": "Fighter removed"}), 200