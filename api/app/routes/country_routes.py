from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Country

country_bp = Blueprint("country", __name__)

@country_bp.route("/countries", methods=["GET"])
@jwt_required()
def get_countries():
    # List all countries in the database
    # Return a list of countries with the following attributes: 
    # id, name, created_at

    return jsonify({"data": ""}), 200
  
@country_bp.route("/country/<int:country_id>", methods=["GET"])
@jwt_required()
def get_country(country_id):
    # List a specific country from the database by id
    # If the country does not exist return a 404 error
    # Return a country with the following attributes: 
    # id, name, created_at

    return jsonify({"data": ""}), 200
  
@country_bp.route("/country", methods=["POST"])
@jwt_required()
def create_country():
    # Create a new country in the database
    # The data should be sent in the request body in JSON format
    # The data should include: name
    # If the country already exists return a 409 error
    # If the data is incorrect return a 400 error
    # If everything is ok create the country 
    # Return the created country with the following attributes: 
    # id, name, created_at

    return jsonify({"data": ""}), 201
  
@country_bp.route("/country/<int:country_id>", methods=["PUT"])
@jwt_required()
def update_country(country_id):
    # Update an existing country in the database
    # The data should be sent in the request body in JSON format
    # The data should include: name
    # If the country does not exist return a 404 error
    # If the data is incorrect return a 400 error
    # If everything is ok update the country 
    # Return the updated country with the following attributes: 
    # id, name, created_at

    return jsonify({"data": ""}), 200
  
@country_bp.route("/country/<int:country_id>", methods=["DELETE"])
@jwt_required()
def delete_country(country_id):
    # Delete a country from the database by id
    # If the country does not exist return a 404 error
    # If everything is ok delete the country 
    # Return a success message

    return jsonify({"data": ""}), 200