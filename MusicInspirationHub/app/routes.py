from flask import Blueprint, jsonify, request
from .models import Usuario, IdeaMusical, RecursoDidactico
from app import db

main = Blueprint('main', __name__)

@main.route('/api/ideas', methods=['GET'])
def get_ideas():
    ideas = IdeaMusical.query.all()
    return jsonify([idea.titulo for idea in ideas])  # Simplificado

@main.route('/api/recursos', methods=['GET'])
def get_recursos():
    recursos = RecursoDidactico.query.all()
    return jsonify([recurso.titulo for recurso in recursos])  # Simplificado
