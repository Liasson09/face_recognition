import cv2
import os
import face_recognition
from app import create_app, db
from app.models import Usuario, Asistencia
from datetime import datetime

# Crear la aplicación y el contexto de la aplicación
app = create_app()
app.app_context().push()

# Codificar los rostros extraídos
imageFacesPath = "faces"

faceEncodings = []
facesName = []

for file_name in os.listdir(imageFacesPath):
    image = cv2.imread(os.path.join(imageFacesPath, file_name))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    f_coding = face_recognition.face_encodings(image, known_face_locations=[(0, 150, 150, 0)])[0]
    faceEncodings.append(f_coding)
    facesName.append(file_name.split(".")[0])

# Video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Detector facial
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    orig = frame.copy()
    faces = faceClassif.detectMultiScale(frame, 1.1, 5)

    for (x, y, w, h) in faces:
        face = orig[y:y + h, x:x + w]
        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        actual_face_encoding = face_recognition.face_encodings(face, known_face_locations=[(0, w, h, 0)])[0]
        result = face_recognition.compare_faces(faceEncodings, actual_face_encoding)

        if True in result:
            index = result.index(True)
            name = facesName[index]
            color = (125, 220, 0)
            
            # Registrar la asistencia en la base de datos
            usuario = Usuario.query.filter_by(nombre=name).first()
            if usuario:
                nueva_asistencia = Asistencia(id_usuario=usuario.id, fecha_hora=datetime.now(), tipo_asistencia="entrada")
                db.session.add(nueva_asistencia)
                db.session.commit()
        else:
            name = "Desconocido"
            color = (50, 50, 255)
        
        cv2.rectangle(frame, (x, y + h), (x + w, y + h + 30), color, -1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y + h + 25), 2, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
