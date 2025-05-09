from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Team, User
from .. import db

team_bp = Blueprint("team", __name__)


@team_bp.route("/teams", methods=["GET"])
@jwt_required()
def get_teams():
    
    # listar todas as equipas exitentes da base de dados
    teams = db.session.query(Team).all()
    # retornar uma lista de equipas com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": 
        [
            {
                "id": team.id,
                "name": team.name,
                "country_id": team.country_id,
                "coach_name": team.coach_name,
                "created_at": team.created_at,
                "updated_at": team.updated_at
            } for team in teams
        ]    
    }), 200

  
@team_bp.route("/team/<int:team_id>", methods=["GET"])
@jwt_required()
def get_team(team_id):
    
    # listar uma equipa especifica da base de dados pelo id
    team = db.session.query(Team).filter_by(id=team_id).first()
    # se a equipa não existir retornar um erro 404
    if not team:
        return jsonify({"error": "Team not found"}), 404
    # retornar uma equipa com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": {
        "id": team.id,
        "name": team.name,
        "country_id": team.country_id,
        "coach_name": team.coach_name,
        "created_at": team.created_at,
        "updated_at": team.updated_at    
    }}), 200

  
@team_bp.route("/team", methods=["POST"])
@jwt_required()
def create_team():
    
    # criar uma nova equipa na base de dados
    # os dados devem ser enviados no corpo da requisição em formato JSON
    body = request.get_json()

    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    
    # os dados devem incluir: nome, id do pais, nome do treinador
    
    name = body.get("name", "").strip()
    country_id = body.get("country_id")
    coach_name = body.get("coach_name", "").strip()
    
    # se a equipa já existir retornar um erro 409
    existing_team = db.session.query(Team).filter_by(name=name).first()
    if existing_team:
        return jsonify({"error": "Team already exists"}), 409
    # se os dados estiverem incorretos retornar um erro 400
    if not name or not country_id or not coach_name:
        return jsonify({"error": "Fields are required"}), 400
    # se estiver tudo ok cria a equipa 
    try:
        new_team = Team(name=name, country_id=country_id, coach_name=coach_name)
        db.session.add(new_team)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error creating team"}), 500
    # retornar a equipa criada com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": {
        "id": new_team.id,
        "name": new_team.name,
        "country_id": new_team.country_id,
        "coach_name": new_team.coach_name,
        "created_at": new_team.created_at,
        "updated_at": new_team.updated_at
    }}), 201
  

@team_bp.route("/team/<int:team_id>", methods=["PUT"])
@jwt_required()
def update_team(team_id):
      
    # atualizar uma equipa existente na base de dados
    # os dados devem ser enviados no corpo da requisição em formato JSON
    body = request.get_json()
    
    if not body:
        return jsonify({"error": "JSON body is required"}), 400
    
    # os dados devem incluir: nome, id do pais, nome do treinador
    name = body.get("name", "").strip()
    country_id = body.get("country_id")
    coach_name = body.get("coach_name", "").strip()
    
    # se a equipa não existir retornar um erro 404
    team = db.session.query(Team).filter_by(id=team_id).first()
    if not team:
        return jsonify({"error": "Team not found"}), 404
    
    # se os dados estiverem incorretos retornar um erro 400
    if not name or not country_id or not coach_name:
        return jsonify({"error": "Fields are required"}), 400
    
    # se estiver tudo ok atualiza a equipa 
    # retornar a equipa atualizada com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": {
        "id": team.id,
        "name": name,
        "country_id": country_id,
        "coach_name": coach_name,
        "created_at": team.created_at,
        "updated_at": team.updated_at
    }}), 200

@team_bp.route("/team/<int:team_id>", methods=["DELETE"])
@jwt_required()
def delete_team(team_id):
    # deletar uma equipa existente na base de dados
    # se a equipa não existir retornar um erro 404
    team = db.session.query(Team).filter_by(id=team_id).first()
    if not team:
        return jsonify({"error": "Team not found"}), 404
    # se estiver tudo ok deleta a equipa 
    try:
        db.session.delete(team)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error deleting team"}), 500
    # retornar uma mensagem de sucesso

    return jsonify({"data": "Record deleted."}), 200
  
# DICA: criem um metodo para pesquisar por id e validar se a equipa existe ou não, 
# e chamem esse metodo nos metodos de update e delete
# para evitar repetição de código