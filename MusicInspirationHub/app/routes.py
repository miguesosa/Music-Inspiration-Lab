from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .models import Usuario
from . import db

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    contraseña = data.get('contraseña')

    if not nombre or not email or not contraseña:
        return jsonify({"msg": "Faltan datos"}), 400

    usuario_existente = Usuario.query.filter_by(email=email).first()
    if usuario_existente:
        return jsonify({"msg": "El usuario ya existe"}), 400

    nueva_contraseña = generate_password_hash(contraseña)
    nuevo_usuario = Usuario(nombre=nombre, email=email, contraseña=nueva_contraseña)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"msg": "Usuario registrado exitosamente"}), 201


@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    contraseña = data.get('contraseña')

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not check_password_hash(usuario.contraseña, contraseña):
        return jsonify({"msg": "Credenciales incorrectas"}), 401

    access_token = create_access_token(identity=usuario.id)

    return jsonify(access_token=access_token), 200


@main.route('/protegido', methods=['GET'])
@jwt_required()
def ruta_protegida():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Bienvenido, usuario {current_user}!"}), 200


@main.route('/test', methods=['GET'])
def test_route():
    return jsonify({"msg": "Ruta de prueba funcionando!"}), 200
