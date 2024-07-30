import numpy as np

with open('fichier.txt', 'r') as fichier :
     contenu = fichier.read()
     print(contenu)

data = np.genfromtxt('Murders.csv', delimiter = ',')
print(data)