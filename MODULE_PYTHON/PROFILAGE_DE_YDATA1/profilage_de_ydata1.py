import pandas as pd
from ydata_profiling import ProfileReport
df = pd.read_csv("EDUCATION_ATTAINMENT.csv")
print(df.head)
print(df.info())
print(df.describe())
pr = ProfileReport(df, title = "Banque Mondiale")
pr.to_file("Banque-mondiale.html")