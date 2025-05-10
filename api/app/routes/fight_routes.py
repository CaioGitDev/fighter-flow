from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Fight
from .. import db

fight_bp = Blueprint("fight", __name__)

@fight_bp.route("/fights", methods=["GET"])
@jwt_required()
def get_fights():
    # List all fights in the database
    fights = db.session.query(Fight).all()
    # Return a list of fights with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": [
        {
            "id": fight.id,
            "fighter_a_id": fight.fighter_a_id,
            "fighter_b_id": fight.fighter_b_id,
            "schedule_date": fight.schedule_date,
            "location": fight.location,
            "rounds": fight.rounds,
            "rounds_minutes": fight.rounds_minutes,
            "created_at": fight.created_at,
            "updated_at": fight.updated_at
        } for fight in fights
    ]}), 200
  
@fight_bp.route("/fight/<int:fight_id>", methods=["GET"])
@jwt_required()
def get_fight(fight_id):
    # List a specific fight from the database by id
    fight = db.session.query(Fight).filter_by(id=fight_id).first()
    # If the fight does not exist return a 404 error
    if not fight:
        return jsonify({"error": "Fight not found"}), 404
    # Return a fight with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": {
        "id": fight.id,
        "fighter_a_id": fight.fighter_a_id,
        "fighter_b_id": fight.fighter_b_id,
        "schedule_date": fight.schedule_date,
        "location": fight.location,
        "rounds": fight.rounds,
        "rounds_minutes": fight.rounds_minutes,
        "created_at": fight.created_at,
        "updated_at": fight.updated_at
    }}), 200
  
@fight_bp.route("/fight", methods=["POST"])
@jwt_required()
def create_fight():
    # Create a new fight in the database
    # The data should be sent in the request body in JSON format
    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    # The data should include: fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes
    fighter_a_id = body.get("fighter_a_id")
    fighter_b_id = body.get("fighter_b_id")
    schedule_date = body.get("schedule_date")
    location = body.get("location")
    rounds = body.get("rounds")
    rounds_minutes = body.get("rounds_minutes")
    
    if not fighter_a_id or not fighter_b_id or not schedule_date or not location or not rounds or not rounds_minutes:
        return jsonify({"error": "All fields are required"}), 400
    
    # If the fight already exists return a 409 error
    existing_fight = db.session.query(Fight).filter_by(fighter_a_id=fighter_a_id, fighter_b_id=fighter_b_id, schedule_date = schedule_date).first()
    # If the data is incorrect return a 400 error
    if existing_fight:
        return jsonify({"error": "Fight already exists"}), 409
    # If everything is ok create the fight 
    try:
        new_fight = Fight(
            fighter_a_id=fighter_a_id,
            fighter_b_id=fighter_b_id,
            schedule_date=schedule_date,
            location=location,
            rounds=rounds,
            rounds_minutes=rounds_minutes
        )
        db.session.add(new_fight)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # Return the created fight with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": {
        "id": new_fight.id,
        "fighter_a_id": new_fight.fighter_a_id,
        "fighter_b_id": new_fight.fighter_b_id,
        "schedule_date": new_fight.schedule_date,
        "location": new_fight.location,
        "rounds": new_fight.rounds,
        "rounds_minutes": new_fight.rounds_minutes,
        "created_at": new_fight.created_at,
        "updated_at": new_fight.updated_at
    }}), 201
  
@fight_bp.route("/fight/<int:fight_id>", methods=["PUT"])
@jwt_required()
def update_fight(fight_id):
    # Update an existing fight in the database
    # The data should be sent in the request body in JSON format
    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    
    # The data should include: fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes
    fighter_a_id = body.get("fighter_a_id")
    fighter_b_id = body.get("fighter_b_id")
    schedule_date = body.get("schedule_date")
    location = body.get("location")
    rounds = body.get("rounds")
    rounds_minutes = body.get("rounds_minutes")
    
    # If the fight does not exist return a 404 error
    fight = db.session.query(Fight).filter_by(id=fight_id).first()
    if not fight:
        return jsonify({"error": "Fight not found"}), 404
    # If the data is incorrect return a 400 error
    if not fighter_a_id or not fighter_b_id or not schedule_date or not location or not rounds or not rounds_minutes:
        return jsonify({"error": "All fields are required"}), 400
    # If everything is ok update the fight 
    try:
        fight.fighter_a_id = fighter_a_id
        fight.fighter_b_id = fighter_b_id
        fight.schedule_date = schedule_date
        fight.location = location
        fight.rounds = rounds
        fight.rounds_minutes = rounds_minutes
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    # Return the updated fight with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": {
        "id": fight.id,
        "fighter_a_id": fight.fighter_a_id,
        "fighter_b_id": fight.fighter_b_id,
        "schedule_date": fight.schedule_date,
        "location": fight.location,
        "rounds": fight.rounds,
        "rounds_minutes": fight.rounds_minutes,
        "created_at": fight.created_at,
        "updated_at": fight.updated_at
    }}), 200
  
@fight_bp.route("/fight/<int:fight_id>", methods=["DELETE"])
@jwt_required()
def delete_fight(fight_id):
    # Delete a fight from the database by id
    fight = db.session.query(Fight).filter_by(id=fight_id).first()
    # If the fight does not exist return a 404 error
    if not fight:
        return jsonify({"error": "Fight not found"}), 404
    # If everything is ok delete the fight 
    try:
        db.session.delete(fight)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    # Return a success message

    return jsonify({"data": "Record Deleted"}), 200