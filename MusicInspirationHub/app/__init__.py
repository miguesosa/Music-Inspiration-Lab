from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    """
    Función que crea y configura la aplicación Flask.
    Inicializa la base de datos, migraciones y JWT.
    """
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:Inspiration2024!@localhost/music_inspiration_hub' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Habilitar el modo de depuración
    app.config['DEBUG'] = True

    # Configuración de JWT
    app.config['JWT_SECRET_KEY'] = 'Salvijwtteama2024'  # Cambia esto por una clave segura en producción

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Importar y registrar las rutas
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Importar modelos después de inicializar 'db'
    from .models import Usuario, IdeaMusical, RecursoDidactico

    return app
