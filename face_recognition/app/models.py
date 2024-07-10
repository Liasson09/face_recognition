from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    tipo_usuario = db.Column(db.String(50), nullable=False)
    correo_electronico = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(100), nullable=False)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_curso = db.Column(db.String(100), nullable=False)
    id_docente = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    tipo_asistencia = db.Column(db.String(50), nullable=False)

class InformeAtencion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    nivel_atencion = db.Column(db.String(50), nullable=False)

class MetodologiaEnsenanza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_metodologia = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)

class AsistenciaMarcada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_estudiante = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha_hora_marcado = db.Column(db.DateTime, nullable=False)
    tipo_marcado = db.Column(db.String(50), nullable=False)