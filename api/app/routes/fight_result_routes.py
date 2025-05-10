from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import FightResult
from .. import db

fight_result_bp = Blueprint("fight_result", __name__)

@fight_result_bp.route("/fight_results", methods=["GET"])
@jwt_required()
def get_fight_results():
    # List all fight results in the database
    results = db.session.query(FightResult).all()
    # Return a list of fight results with the following attributes: 
    # id, fight_id, winner_id, method, round, time, created_at and updated_at

    return jsonify({"data": [
        {
            "id": result.id,
            "fight_id": result.fight_id,
            "winner_id": result.winner_id,
            "method": result.method,
            "round": result.round,
            "time": result.time,
            "created_at": result.created_at,
            "updated_at": result.updated_at
        } for result in results
    ]}), 200
  
@fight_result_bp.route("/fight_result/<int:fight_result_id>", methods=["GET"])
@jwt_required()
def get_fight_result(fight_result_id):
    # List a specific fight result from the database by id
    result = db.session.query(FightResult).filter_by(id=fight_result_id).first()
    # If the fight result does not exist return a 404 error
    if not result:
        return jsonify({"error": "Fight result not found"}), 404
    # Return a fight result with the following attributes: 
    # id, fight_id, winner_id, method, round, time, created_at and updated_at

    return jsonify({"data": {
        "id": result.id,
        "fight_id": result.fight_id,
        "winner_id": result.winner_id,
        "method": result.method,
        "round": result.round,
        "time": result.time,
        "created_at": result.created_at,
        "updated_at": result.updated_at    
    }}), 200
  
@fight_result_bp.route("/fight_result", methods=["POST"])
@jwt_required()
def create_fight_result():
    # Create a new fight result in the database
    # The data should be sent in the request body in JSON format
    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    # The data should include: fight_id, winner_id, method, round, time
    fight_id = body.get("fight_id")
    winner_id = body.get("winner_id")
    method = body.get("method")
    fight_round = body.get("round")
    time = body.get("time")
    
    if not fight_id or not winner_id or not method or not round or not time:
        return jsonify({"error": "All fields are required"}), 400
    if method not in ["KO", "TKO", "Submission", "Decision"]:
        return jsonify({"error": "Method must be one of: KO, TKO, Submission, Decision"}), 400
    if fight_round < 1 or fight_round > 12:
        return jsonify({"error": "Round must be between 1 and 12"}), 400
    if time < 0 or time > 300:
        return jsonify({"error": "Time must be between 0 and 300 seconds"}), 400
    
    # If the data is incorrect return a 400 error
    if not fight_id or not winner_id or not method or not fight_round or not time:
        return jsonify({"error": "All fields are required"}), 400
    # If everything is ok create the fight result 
    try:
        new_result = FightResult(
            fight_id=fight_id,
            winner_id=winner_id,
            method=method,
            round=fight_round,
            time=time
        )
        db.session.add(new_result)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating fight result"}), 500
    # Return the created fight result with the following attributes: 
    # id, fight_id, winner_id, method, round, time, created_at and updated_at

    return jsonify({"data": {
        "id": new_result.id,
        "fight_id": new_result.fight_id,
        "winner_id": new_result.winner_id,
        "method": new_result.method,
        "round": new_result.round,
        "time": new_result.time,
        "created_at": new_result.created_at,
        "updated_at": new_result.updated_at
    }}), 201
  
@fight_result_bp.route("/fight_result/<int:fight_result_id>", methods=["PUT"])
@jwt_required()
def update_fight_result(fight_result_id):
    # Update an existing fight result in the database
    # The data should be sent in the request body in JSON format
    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    # The data should include: fight_id, winner_id, method, round, time
    fight_id = body.get("fight_id")
    winner_id = body.get("winner_id")
    method = body.get("method")
    fight_round = body.get("round")
    time = body.get("time")
    
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

