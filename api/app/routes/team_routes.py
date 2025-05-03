from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Team, User

team_bp = Blueprint("team", __name__)


@team_bp.route("/teams", methods=["GET"])
@jwt_required()
def get_teams():
    
    # listar todas as equipas exitentes da base de dados
    # retornar uma lista de equipas com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": ""}), 200

  
@team_bp.route("/team/<int:team_id>", methods=["GET"])
@jwt_required()
def get_team(team_id):
    
    # listar uma equipa especifica da base de dados pelo id
    # se a equipa não existir retornar um erro 404
    # retornar uma equipa com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": ""}), 200

  
@team_bp.route("/team", methods=["POST"])
@jwt_required()
def create_team():
    
    # criar uma nova equipa na base de dados
    # os dados devem ser enviados no corpo da requisição em formato JSON
    # os dados devem incluir: nome, id do pais, nome do treinador
    # se a equipa já existir retornar um erro 409
    # se os dados estiverem incorretos retornar um erro 400
    # se estiver tudo ok cria a equipa 
    # retornar a equipa criada com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": ""}), 201
  

@team_bp.route("/team/<int:team_id>", methods=["PUT"])
@jwt_required()
def update_team(team_id):
      
    # atualizar uma equipa existente na base de dados
    # os dados devem ser enviados no corpo da requisição em formato JSON
    # os dados devem incluir: nome, id do pais, nome do treinador
    # se a equipa não existir retornar um erro 404
    # se os dados estiverem incorretos retornar um erro 400
    # se estiver tudo ok atualiza a equipa 
    # retornar a equipa atualizada com os seguintes atributos: 
    # id, nome, id do pais, nome do treinador, data de criação e data de atualização

    return jsonify({"data": ""}), 200

@team_bp.route("/team/<int:team_id>", methods=["DELETE"])
@jwt_required()
def delete_team(team_id):
    # deletar uma equipa existente na base de dados
    # se a equipa não existir retornar um erro 404
    # se estiver tudo ok deleta a equipa 
    # retornar uma mensagem de sucesso

    return jsonify({"data": ""}), 200
  
# DICA: criem um metodo para pesquisar por id e validar se a equipa existe ou não, 
# e chamem esse metodo nos metodos de update e delete
# para evitar repetição de código