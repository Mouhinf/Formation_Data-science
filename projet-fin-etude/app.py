import streamlit as st
import cv2
import numpy as np
from keras.applications import VGG16
from keras.preprocessing.image import img_to_array
from mtcnn.mtcnn import MTCNN

# Charger le modèle de détection de visage et VGG16
detector = MTCNN()
model = VGG16(weights='imagenet', include_top=False)

# Fonction pour extraire les visages
def extract_faces(image):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(img_rgb)
    extracted_faces = []

    for face in faces:
        x, y, width, height = face['box']
        face_image = img_rgb[y:y + height, x:x + width]
        if face_image.shape[0] > 0 and face_image.shape[1] > 0:
            extracted_faces.append(face_image)

    return extracted_faces

# Fonction pour extraire les caractéristiques du visage
def extract_features(face_images):
    features = []
    for img in face_images:
        img_resized = cv2.resize(img, (224, 224))
        img_array = img_to_array(img_resized)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalisation
        feature = model.predict(img_array)
        features.append(feature.flatten())  # Aplatir les caractéristiques
    return np.array(features)

# Titre de l'application
st.title("Système de Reconnaissance Faciale")

uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "png"])

if uploaded_file is not None:
    # Lire l'image téléchargée
    image = np.array(bytearray(uploaded_file.read()))
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    st.image(image, caption='Image téléchargée.', use_column_width=True)

    # Extraction des visages
    faces = extract_faces(image)

    if faces:
        st.write(f"{len(faces)} visage(s) détecté(s)")

        # Affichage des visages extraits
        for i, face in enumerate(faces):
            st.image(face, caption=f'Visage {i + 1}', use_column_width=True)

        # Extraction des caractéristiques pour chaque visage
        features = extract_features(faces)
        st.write("Caractéristiques extraites des visages :")
        st.write(features)  # Afficher les caractéristiques extraites
    else:
        st.write("Aucun visage détecté.")
