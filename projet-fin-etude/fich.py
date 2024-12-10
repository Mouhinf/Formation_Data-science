import cv2
import os
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

# Chargement du classificateur Cascade HAAR
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def extract_faces_haar(image_path, output_folder):
    # Chargement de l'image
    img = cv2.imread(image_path)
    if img is None:  # Vérification si l'image est correctement chargée
        print(f"Erreur lors du chargement de l'image: {image_path}")
        return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for i, (x, y, w, h) in enumerate(faces):
        face = img[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(output_folder, f'face_{i}.jpg'), face)

# Exemple d'utilisation
input_folder = 'data/images/'
output_folder = 'data/faces_haar/'

# Vérification de l'existence du dossier d'entrée
if not os.path.exists(input_folder):
    print(f"Le dossier {input_folder} n'existe pas. Veuillez le créer et y ajouter des images.")
else:
    # Création du dossier de sortie s'il n'existe pas
    os.makedirs(output_folder, exist_ok=True)

    # Traitement des images dans le dossier d'entrée
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            extract_faces_haar(os.path.join(input_folder, filename), output_folder)
            
from keras.applications import VGG16
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

# Charger le modèle VGG16 pré-entraîné sans la couche supérieure (include_top=False)
model = VGG16(weights='imagenet', include_top=False)

def extract_features(image_paths):
    features = []
    for path in image_paths:
        img = load_img(path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalisation des pixels entre 0 et 1
        feature = model.predict(img_array)
        features.append(feature.flatten())  # Aplatir les caractéristiques pour obtenir un vecteur
    return np.array(features)

# Exemple d'utilisation
output_folder = 'data/images/'  # Remplacer par le chemin réel du dossier des images
face_images = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith('.jpg')]
features = extract_features(face_images)
