from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Country
from .. import db

country_bp = Blueprint("country", __name__)

@country_bp.route("/countries", methods=["GET"])
@jwt_required()
def get_countries():
    # List all countries in the database
    # Return a list of countries with the following attributes: 
    # id, name, created_at
    
    countries = db.session.query(Country).all()
    countries_list = [
        {
            "id": country.id,
            "name": country.name,
            "created_at": country.created_at
        } for country in countries
    ]

    return jsonify({"data": countries_list}), 200
  
@country_bp.route("/country/<int:country_id>", methods=["GET"])
@jwt_required()
def get_country(country_id):
    # List a specific country from the database by id
    country = db.session.query(Country).filter_by(id=country_id).first()
    # If the country does not exist return a 404 error
    if not country:
        return jsonify({"error": "Country not found"}), 404
    
    # Return a country with the following attributes: 
    # id, name, created_at
    return jsonify({"data": {
        "id": country.id,
        "name": country.name,
        "created_at": country.created_at
    }}), 200
  
@country_bp.route("/country", methods=["POST"])
@jwt_required()
def create_country():
    body = request.get_json()

    if not body:
        return jsonify({"error": "JSON body is required"}), 400

    name = body.get("name", "").strip()

    if not name:
        return jsonify({"error": "Name is required"}), 400

    if len(name) < 3 or len(name) > 50:
        return jsonify({"error": "Name must be between 3 and 50 characters"}), 400

    try:
        existing_country = db.session.query(Country).filter_by(name=name).first()
        if existing_country:
            return jsonify({"error": "Country already exists"}), 409

        new_country = Country(name=name)
        db.session.add(new_country)
        db.session.commit()

        return jsonify({
            "data": {
                "id": new_country.id,
                "name": new_country.name,
                "created_at": new_country.created_at
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred while creating the country: {str(e)}"}), 500

    finally:
        db.session.close()
  
@country_bp.route("/country/<int:country_id>", methods=["PUT"])
@jwt_required()
def update_country(country_id):
    # Update an existing country in the database
    country = db.session.query(Country).filter_by(id=country_id).first()
    
    # If the country does not exist return a 404 error
    if not country:
        return jsonify({"error": "Country not found"}), 404
    
    # The data should be sent in the request body in JSON format
    body = request.get_json()
    
    if not body:
        return jsonify({"error": "JSON body is required"}), 400

    # The data should include: name
    name = body.get("name", "").strip()
    
    # If the data is incorrect return a 400 error
    if not name:
        return jsonify({"error": "Name is required"}), 400
    
    # If everything is ok update the country 
    if len(name) < 3 or len(name) > 50:
        return jsonify({"error": "Name must be between 3 and 50 characters"}), 400
    
    #update the country name
    country.name = name
    db.session.commit()
        
    # Return the updated country with the following attributes: 
    # id, name, created_at
    return jsonify({"data": {
        "id": country.id,
        "name": country.name,
        "created_at": country.created_at    
    }}), 200
  
@country_bp.route("/country/<int:country_id>", methods=["DELETE"])
@jwt_required()
def delete_country(country_id):
    # Delete a country from the database by id
    
    country = db.session.query(Country).filter_by(id=country_id).first()
    
    # If the country does not exist return a 404 error
    if not country:
        return jsonify({"error": "Country not found"}), 404
    
   
    # If everything is ok delete the country 
    db.session.delete(country)
    db.session.commit()
    
    # Return a success message
    return jsonify({"data": "Country deleted successfully"}), 200