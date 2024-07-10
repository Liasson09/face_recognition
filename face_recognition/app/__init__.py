from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Usar configuración desde config.py

    db.init_app(app)

    with app.app_context():
        from app.models import Usuario, Curso, Asistencia, InformeAtencion, MetodologiaEnsenanza, AsistenciaMarcada
        db.create_all()

    return app