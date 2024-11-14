import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Initialisation du détecteur de visage
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Titre de l'application
st.title("Application de Détection de Visage")

# Instructions pour l'utilisateur
st.write("""
Cette application détecte les visages dans une image téléchargée. Suivez les étapes ci-dessous :
1. Téléchargez une image en cliquant sur "Browse files".
2. Ajustez les paramètres pour affiner la détection de visage.
3. Choisissez la couleur du rectangle autour des visages détectés.
4. Cliquez sur "Détecter les visages" pour voir le résultat.
5. Vous pouvez sauvegarder l'image avec les visages détectés sur votre appareil.
""")

# Téléchargement de l'image
uploaded_file = st.file_uploader("Téléchargez une image", type=["jpg", "jpeg", "png"])

# Paramètres de détection
scale_factor = st.slider("Facteur d'échelle (scaleFactor)", min_value=1.1, max_value=2.0, step=0.1, value=1.1)
min_neighbors = st.slider("Nombre minimum de voisins (minNeighbors)", min_value=3, max_value=10, step=1, value=5)
rect_color = st.color_picker("Choisissez la couleur du rectangle", "#FF0000")
color = tuple(int(rect_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

if uploaded_file is not None:
    # Conversion de l'image
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Bouton pour détecter les visages
    if st.button("Détecter les visages"):
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=scale_factor,
            minNeighbors=min_neighbors
        )

        # Dessine les rectangles autour des visages
        for (x, y, w, h) in faces:
            cv2.rectangle(image_np, (x, y), (x + w, y + h), color, 2)

        # Affichage du résultat
        st.image(image_np, caption="Image avec visages détectés", use_column_width=True)

        # Bouton pour sauvegarder l'image
        if st.button("Sauvegarder l'image avec les visages détectés"):
            cv2.imwrite("detected_faces.jpg", cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))
            st.write("Image sauvegardée sous le nom 'detected_faces.jpg'.")

