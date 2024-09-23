from flask import Blueprint, jsonify, request
from .models import Usuario, IdeaMusical, RecursoDidactico
from . import db  # Importación relativa

main = Blueprint('main', __name__)

# Ruta raíz de prueba
@main.route('/', methods=['GET'])
def index():
    print("Accediendo a la ruta raíz")  # Mensaje de depuración
    return "Bienvenido al Music Inspiration Hub"

# Obtener todas las ideas musicales
@main.route('/api/ideas', methods=['GET'])
def get_ideas():
    try:
        ideas = IdeaMusical.query.all()
        return jsonify([idea.titulo for idea in ideas])  # Devolver los títulos de las ideas
    except Exception as e:
        print(f"Error al obtener las ideas: {e}")
        return jsonify({'error': 'No se pudieron obtener las ideas musicales.'}), 500

# Obtener todos los recursos didácticos
@main.route('/api/recursos', methods=['GET'])
def get_recursos():
    try:
        recursos = RecursoDidactico.query.all()
        return jsonify([recurso.titulo for recurso in recursos])  # Devolver los títulos de los recursos
    except Exception as e:
        print(f"Error al obtener los recursos: {e}")
        return jsonify({'error': 'No se pudieron obtener los recursos didácticos.'}), 500

# Añadir una nueva idea musical
@main.route('/api/ideas', methods=['POST'])
def add_idea():
    try:
        data = request.get_json()
        print(f"Datos recibidos para nueva idea: {data}")  # Depuración
        new_idea = IdeaMusical(titulo=data['titulo'])  # Crear nueva idea con el título recibido
        db.session.add(new_idea)
        db.session.commit()
        return jsonify({'message': 'Idea añadida exitosamente'}), 201
    except Exception as e:
        print(f"Error al añadir la idea: {e}")
        return jsonify({'error': 'Ocurrió un error al añadir la idea.'}), 500

# Añadir un nuevo recurso didáctico
@main.route('/api/recursos', methods=['POST'])
def add_recurso():
    try:
        data = request.get_json()
        print(f"Datos recibidos para nuevo recurso: {data}")  # Depuración
        new_recurso = RecursoDidactico(titulo=data['titulo'])  # Crear nuevo recurso con el título recibido
        db.session.add(new_recurso)
        db.session.commit()
        return jsonify({'message': 'Recurso añadido exitosamente'}), 201
    except Exception as e:
        print(f"Error al añadir el recurso: {e}")
        return jsonify({'error': 'Ocurrió un error al añadir el recurso.'}), 500
