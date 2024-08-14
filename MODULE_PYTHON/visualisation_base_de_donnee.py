import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Popular_Baby_Names.csv")
print(df.head())
plt.bar(df['Year of Birth'], df['Count'], edgecolor = "black")
plt.title("Diagramme en barre des années aniversaire en fonction des count")
plt.xlabel("Année d'anniversaire")
plt.ylabel("Nombre de bébé")
plt.show()
