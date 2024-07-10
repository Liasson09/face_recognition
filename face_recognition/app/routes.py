from flask import Blueprint, render_template
from app.models import Asistencia

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/asistencias')
def asistencias():
    asistencias = Asistencia.query.all()
    return render_template('asistencias.html', asistencias=asistencias)