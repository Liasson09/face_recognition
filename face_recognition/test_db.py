from app import create_app, db
from app.models import Usuario

app = create_app()

with app.app_context():
    # Verificar la existencia de la tabla Usuario
    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()
    if 'Usuario' in tables:
        print("La conexión es correcta y la tabla 'Usuario' existe.")
    else:
        print("La tabla 'Usuario' no existe. Verifica la configuración y la creación de las tablas.")