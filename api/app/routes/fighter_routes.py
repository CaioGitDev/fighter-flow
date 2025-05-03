from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Fighter

fighter_bp = Blueprint("fighter", __name__)

@fighter_bp.route("/fighters", methods=["GET"])
@jwt_required()
def get_fighters():
    # List all fighters in the database
    # Return a list of fighters with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fighter_bp.route("/fighter/<int:fighter_id>", methods=["GET"])
@jwt_required()
def get_fighter(fighter_id):
    # List a specific fighter from the database by id
    # If the fighter does not exist, return a 404 error
    # Return a fighter with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fighter_bp.route("/fighter", methods=["POST"])
@jwt_required()
def create_fighter():
    # Create a new fighter in the database
    # The data should be sent in the request body in JSON format
    # The data should include: first name, last name, nickname, weight, team id, wins, losses, draws, active status
    # If the fighter already exists, return a 409 error
    # If the data is incorrect, return a 400 error
    # If everything is ok, create the fighter 
    # Return the created fighter with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": ""}), 201
  
@fighter_bp.route("/fighter/<int:fighter_id>", methods=["PUT"])
@jwt_required()
def update_fighter(fighter_id):
    # Update an existing fighter in the database
    # The data should be sent in the request body in JSON format
    # The data should include: first name, last name, nickname, weight, team id, wins, losses, draws, active status
    # If the fighter does not exist, return a 404 error
    # If the data is incorrect, return a 400 error
    # If everything is ok, update the fighter 
    # Return the updated fighter with the following attributes: 
    # id, first name, last name, nickname, weight, team id, wins, 
    # losses, draws, active status, created_at and updated_at

    return jsonify({"data": ""}), 200
  
@fighter_bp.route("/fighter/<int:fighter_id>", methods=["DELETE"])
@jwt_required()
def delete_fighter(fighter_id):
    # Delete a fighter from the database by id
    # If the fighter does not exist, return a 404 error
    # If everything is ok, delete the fighter 
    # Return a success message

    return jsonify({"data": ""}), 200