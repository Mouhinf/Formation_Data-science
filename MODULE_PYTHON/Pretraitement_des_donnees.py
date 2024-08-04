import pandas as pd
client_0_bills = pd.read_csv("STEG_BILLING_HISTORY.csv")
print(client_0_bills)
print(client_0_bills.head(10))
print(type(client_0_bills))
client_0_bills.info()
client_0_bills.describe()
print(client_0_bills.isnull().sum())
client_0_bills.describe()