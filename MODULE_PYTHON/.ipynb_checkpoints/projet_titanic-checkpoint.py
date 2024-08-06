import pandas as pd

tit = pd.read_csv("titanic-passengers.csv", delimiter = ";")

print(tit.head(20)) 
print(tit.info())
print(tit.describe())
print(tit.isnull().sum())
tit.fillna(tit.mean(), inplace=True)
tit.fillna("Inconnu", inplace=True)
tit.dropna(thresh = len(tit) * 0.5, axis = 1, inplace = True)
tit.dropna(thresh = len(tit.columns) * 0.5, axis = 0, inplace = True)
print(tit.head(20))
tit.drop_duplicates(inplace = True)
print(tit.info())
print(tit.describe())
print(tit.sample(10))
