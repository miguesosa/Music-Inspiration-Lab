from . import db  # Importación relativa

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    contraseña = db.Column(db.String(128))

class IdeaMusical(db.Model):
    __tablename__ = 'ideas_musicales'  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    descripcion = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

class RecursoDidactico(db.Model):
    __tablename__ = 'recursos_didacticos'  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    tipo = db.Column(db.String(50))  # Ej: video, artículo
    url = db.Column(db.String(200))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
