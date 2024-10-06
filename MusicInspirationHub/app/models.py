from . import db  # Importación relativa

class Usuario(db.Model):
    """
    Modelo para la tabla de usuarios.

    Attributes:
        id (int): Identificador único del usuario.
        nombre (str): Nombre del usuario.
        email (str): Email único del usuario.
        contraseña (str): Contraseña del usuario (almacenada de manera segura).
    """
    __tablename__ = 'usuarios'  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)  # Hash de contraseña

class IdeaMusical(db.Model):
    """
    Modelo para la tabla de ideas musicales.

    Attributes:
        id (int): Identificador único de la idea musical.
        titulo (str): Título de la idea musical.
        descripcion (str): Descripción de la idea musical.
        usuario_id (int): Referencia al usuario que creó la idea.
    """
    __tablename__ = 'ideas_musicales'  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    descripcion = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))  # Relación con la tabla usuarios

class RecursoDidactico(db.Model):
    """
    Modelo para la tabla de recursos didácticos.

    Attributes:
        id (int): Identificador único del recurso didáctico.
        titulo (str): Título del recurso didáctico.
        tipo (str): Tipo del recurso (ej. video, artículo).
        url (str): URL del recurso didáctico.
        usuario_id (int): Referencia al usuario que creó el recurso.
    """
    __tablename__ = 'recursos_didacticos'  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    tipo = db.Column(db.String(50))  # Ej: video, artículo
    url = db.Column(db.String(200))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))  # Relación con la tabla usuarios
