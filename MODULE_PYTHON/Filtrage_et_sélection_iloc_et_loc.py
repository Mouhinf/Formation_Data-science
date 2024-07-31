import pandas as pd
data = {'Nom': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'], 
        'Département': ['IT', 'Marketing', 'Ventes', 'IT', 'Finances', 'Marketing'], 
        'Âge': [30, 40, 25, 35, 45, 28], 
        'Sexe': ['Homme', 'Femme', 'Homme', 'Femme', 'Homme', 'Femme'], 
        'Salaire': [50000, 60000, 45000, 55000, 70000, 55000], 
        'Expérience': [3, 7, 2, 5, 10, 4]} 
employee_df = pd.DataFrame(data)
print(employee_df)
employee_df.index = ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa']
employee_df.loc(['John', 'Mary', 'Bob'])