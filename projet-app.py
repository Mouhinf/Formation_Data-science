from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle

app = Flask(__name__)

# Charger vos données
data = pd.read_csv('final_Data.csv')

# Prétraitement et entraînement du modèle au chargement initial
def preprocess_and_train():
    # Vos étapes de prétraitement ici
    data_cleaned = data.copy()
    columns_to_clean = ['Production', 'diff', 'stock', 'pourcent_fuite']
    for col in columns_to_clean:
        data_cleaned[col] = data_cleaned[col].str.replace(r'[^\d\.-]', '', regex=True).astype(float)
        
    data_cleaned['fuite'] = data_cleaned['fuite'].map({'oui': 1, 'non': 0})

    X = data_cleaned.drop(columns=['fuite'])
    y = data_cleaned['fuite']
    
    # Séparer et normaliser les données
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Entraîner le modèle
    model = SVC(kernel='rbf', C=1, gamma='scale', random_state=42)
    model.fit(X_scaled, y)

    # Sauvegarder le modèle et le scaler
    with open('svm_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
    with open('scaler.pkl', 'wb') as scaler_file:
        pickle.dump(scaler, scaler_file)

# Entraîner le modèle (cela ne doit être exécuté qu'une seule fois)
preprocess_and_train()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.form.to_dict()
    
    # Convertir les données d'entrée en DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Charger le modèle et le scaler
    with open('svm_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    # Prétraiter les données d'entrée
    cols_to_clean = ['Production', 'diff', 'stock', 'pourcent_fuite']
    for col in cols_to_clean:
        input_df[col] = input_df[col].str.replace(r'[^\d\.-]', '', regex=True).astype(float)
        
    input_scaled = scaler.transform(input_df)

    # Effectuer la prédiction
    prediction = model.predict(input_scaled)
    result = 'oui' if prediction[0] == 1 else 'non'
    
    return render_template('results.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

