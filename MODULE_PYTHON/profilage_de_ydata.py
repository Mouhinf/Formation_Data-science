import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv("Tunisair_flights_dataset.csv")
print(df.head(20))
print(df.info())
print(df.isnull().sum())
print(df.describe())
pr = ProfileReport(df, title = "tunisie flights")
pr.to_file("Profilage de pandas.html")
