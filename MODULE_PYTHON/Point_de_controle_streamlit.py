import pandas as pd
import numpy as np
df = pd.read_csv('Expresso_churn_dataset.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

# from ydata_profiling import ProfileReport

# profile = ProfileReport(df, title="Expresso Churn Dataset Report", explorative=True)
# profile.to_file("expresso_churn_report.html")
df = df.drop_duplicates()

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
df['user_id'] = label_encoder.fit_transform(df['user_id'])
df['REGION'] = label_encoder.fit_transform(df['REGION'])
df['TENURE'] = label_encoder.fit_transform(df['TENURE'])
df['MRG'] = label_encoder.fit_transform(df['MRG'])
df['TOP_PACK'] = label_encoder.fit_transform(df['TOP_PACK'])

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer



X = df.drop(['user_id', 'REGION'], axis=1)
y = df['CHURN']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
imputer = SimpleImputer(strategy="mean")
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

import streamlit as st
import pandas as pd
import joblib  

model = joblib.load('your_model.pkl')

st.title("Expresso Churn Prediction App")

feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")

if st.button("Prédire"):
    features = pd.DataFrame([[feature1, feature2]], columns=['feature1', 'feature2'])
    prediction = model.predict(features)
    st.write("Prédiction :", prediction)
