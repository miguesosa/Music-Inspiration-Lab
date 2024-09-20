from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/music_inspiration_hub'  # Cambia por tus credenciales
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'tu_clave_secreta'  # Cambia esto por una clave secreta real

    # Inicializar extensiones
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    # Importar y registrar las rutas
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app