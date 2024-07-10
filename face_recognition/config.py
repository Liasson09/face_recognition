import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Users/rosa_/OneDrive/Escritorio/face_recognition/BD_asistencia.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False