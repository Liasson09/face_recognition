from app import create_app, db
from app.models import Usuario, Curso, Asistencia, InformeAtencion, MetodologiaEnsenanza, AsistenciaMarcada

app = create_app()

with app.app_context():
    db.drop_all()  # Esto eliminará todas las tablas existentes
    db.create_all()  # Esto creará todas las tablas definidas en los modelos
    print("Todas las tablas han sido creadas correctamente.")