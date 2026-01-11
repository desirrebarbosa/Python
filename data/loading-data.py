import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
df = pd.read_csv(filename)
print(df.head())

x = df[['Quantity']]
print(x)