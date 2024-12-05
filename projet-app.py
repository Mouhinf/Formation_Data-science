from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle
import re

app = Flask(__name__)

# Charger vos données
data = pd.read_csv('final_data - Feuille 1.csv')

def preprocess_and_train():
    try:
        # Prétraitement des données
        columns_to_clean = ['Production', 'diff', 'stock', 'pourcent_fuite']
        data_cleaned = data.copy()
        for col in columns_to_clean:
            data_cleaned[col] = data_cleaned[col].replace(r'[^\d\.-]', '', regex=True)
            data_cleaned[col] = data_cleaned[col].str.replace('\u202f', '', regex=True)
            data_cleaned[col] = data_cleaned[col].str.replace(',', '.')
            data_cleaned[col] = pd.to_numeric(data_cleaned[col], errors='coerce')
        
        # Vérifier les valeurs NaN
        if data_cleaned[columns_to_clean].isnull().any().any():
            raise ValueError("Des valeurs non convertibles ont été détectées dans les colonnes à nettoyer.")
        
        # Conversion de la colonne cible
        data_cleaned['fuite'] = data['fuite'].map({'oui': 1, 'non': 0})
        
        # Séparer X et y
        X = data_cleaned.drop(columns=['fuite'])
        y = data_cleaned['fuite']
        
        # Normalisation
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Modèle SVM
        model = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)
        model.fit(X_scaled, y)
        
        # Sauvegarde du modèle et du scaler
        with open('svm_model.pkl', 'wb') as model_file:
            pickle.dump(model, model_file)
        with open('scaler.pkl', 'wb') as scaler_file:
            pickle.dump(scaler, scaler_file)
    
    except Exception as e:
        print(f"Erreur lors de l'entraînement initial : {e}")
