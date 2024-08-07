import pandas as pd
from ydata_profiling import ProfileReport

# Chargement de votre DataFrame
df = pd.read_csv("Popular_Baby_Names.csv")

# Génération du rapport de profilage sans l'argument 'title'
profile = ProfileReport(df, explorative=True)

# Exportation du rapport au format HTML
profile.to_file("report.html")
