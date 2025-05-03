from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Fight

fight_bp = Blueprint("fight", __name__)

@fight_bp.route("/fights", methods=["GET"])
@jwt_required()
def get_fights():
    # List all fights in the database
    # Return a list of fights with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fight_bp.route("/fight/<int:fight_id>", methods=["GET"])
@jwt_required()
def get_fight(fight_id):
    # List a specific fight from the database by id
    # If the fight does not exist return a 404 error
    # Return a fight with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fight_bp.route("/fight", methods=["POST"])
@jwt_required()
def create_fight():
    # Create a new fight in the database
    # The data should be sent in the request body in JSON format
    # The data should include: fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes
    # If the fight already exists return a 409 error
    # If the data is incorrect return a 400 error
    # If everything is ok create the fight 
    # Return the created fight with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": ""}), 201
  
@fight_bp.route("/fight/<int:fight_id>", methods=["PUT"])
@jwt_required()
def update_fight(fight_id):
    # Update an existing fight in the database
    # The data should be sent in the request body in JSON format
    # The data should include: fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes
    # If the fight does not exist return a 404 error
    # If the data is incorrect return a 400 error
    # If everything is ok update the fight 
    # Return the updated fight with the following attributes: 
    # id, fighter_a_id, fighter_b_id, schedule_date, location, rounds, rounds_minutes, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fight_bp.route("/fight/<int:fight_id>", methods=["DELETE"])
@jwt_required()
def delete_fight(fight_id):
    # Delete a fight from the database by id
    # If the fight does not exist return a 404 error
    # If everything is ok delete the fight 
    # Return a success message

    return jsonify({"data": ""}), 200