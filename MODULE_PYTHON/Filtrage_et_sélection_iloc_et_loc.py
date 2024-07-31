import pandas as pd
data = {'Nom': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'], 
        'Département': ['IT', 'Marketing', 'Ventes', 'IT', 'Finances', 'Marketing'], 
        'Âge': [30, 40, 25, 35, 45, 28], 
        'Sexe': ['Homme', 'Femme', 'Homme', 'Femme', 'Homme', 'Femme'], 
        'Salaire': [50000, 60000, 45000, 55000, 70000, 55000], 
        'Expérience': [3, 7, 2, 5, 10, 4]} 
employee_df = pd.DataFrame(data)
print(employee_df)
df = employee_df.iloc[0:2]
print("Voici la sélection des 3 premieres lignes du dataframe :")
print(df)
employee_df.index = ['IT', 'Marketing', 'Ventes', 'IT', 'Finances', 'Marketing']
print("Voici toutes les lignes du département Marketing :")
dr = employee_df.loc["Marketing", :]
print(dr)

dm = employee_df.iloc[0:4, 2:4]
print("Voici la sélection des colonnes Ages et Sexe pour les 4 premieres lignes du dataframe :")
print(dm)

employee_df.index = ['Nom', 'Département', 'Âge', 'Sexe', 'Salaire', 'Expérience']
dn = employee_df.loc["Salaire", "Expérience"]
print("Voici les colonnes des salaires et expérience pour toutes les lignes où le sexe est homme")
print(dn)