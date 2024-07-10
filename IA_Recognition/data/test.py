from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os

# Cargar el clasificador de caras
cascade_path = 'data/haarcascade_frontalface_default.xml'
if not os.path.exists(cascade_path):
    raise FileNotFoundError(f"No se encontró el archivo {cascade_path}")

facesdetect = cv2.CascadeClassifier(cascade_path)

# Cargar los datos y etiquetas
names_path = 'data/names.pkl'
faces_data_path = 'data/faces_data.pkl'
if not os.path.exists(names_path) or not os.path.exists(faces_data_path):
    raise FileNotFoundError("No se encontraron los archivos de datos")

with open(names_path, 'rb') as f:
    LABELS = pickle.load(f)
with open(faces_data_path, 'rb') as f:
    FACES = pickle.load(f)

# Entrenar el modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# Iniciar la captura de video
video = cv2.VideoCapture(0)
if not video.isOpened():
    raise Exception("No se pudo abrir la cámara")

while True:
    ret, frame = video.read()
    if not ret:
        print("Error al capturar el frame")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facesdetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w, :]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten()            
        resized_img = resized_img.reshape(1, -1)
        output = knn.predict(resized_img)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 1)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (50,50,255),2)
        cv2.rectangle(frame, (x,y-40), (x+w,y), (50,50,255),-1)

        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

