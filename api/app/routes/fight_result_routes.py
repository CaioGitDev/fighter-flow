from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import FightResult

fight_result_bp = Blueprint("fight_result", __name__)

@fight_result_bp.route("/fight_results", methods=["GET"])
@jwt_required()
def get_fight_results():
    # List all fight results in the database
    # Return a list of fight results with the following attributes: 
    # id, fight_id, winner_id, method, round, time, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fight_result_bp.route("/fight_result/<int:fight_result_id>", methods=["GET"])
@jwt_required()
def get_fight_result(fight_result_id):
    # List a specific fight result from the database by id
    # If the fight result does not exist return a 404 error
    # Return a fight result with the following attributes: 
    # id, fight_id, winner_id, method, round, time, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fight_result_bp.route("/fight_result", methods=["POST"])
@jwt_required()
def create_fight_result():
    # Create a new fight result in the database
    # The data should be sent in the request body in JSON format
    # The data should include: fight_id, winner_id, method, round, time
    # If the fight result already exists return a 409 error
    # If the data is incorrect return a 400 error
    # If everything is ok create the fight result 
    # Return the created fight result with the following attributes: 
    # id, fight_id, winner_id, method, round, time, created_at and updated_at

    return jsonify({"data": ""}), 201
  
@fight_result_bp.route("/fight_result/<int:fight_result_id>", methods=["PUT"])
@jwt_required()
def update_fight_result(fight_result_id):
    # Update an existing fight result in the database
    # The data should be sent in the request body in JSON format
    # The data should include: fight_id, winner_id, method, round, time
    # If the fight result does not exist return a 404 error
    # If the data is incorrect return a 400 error
    # If everything is ok update the fight result 
    # Return the updated fight result with the following attributes: 
    # id, fight_id, winner_id, method, round, time, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fight_result_bp.route("/fight_result/<int:fight_result_id>", methods=["DELETE"])
@jwt_required()
def delete_fight_result(fight_result_id):
    # Delete a fight result from the database by id
    # If the fight result does not exist return a 404 error
    # If everything is ok delete the fight result 
    # Return a success message

    return jsonify({"message": "Fight result deleted successfully"}), 200

