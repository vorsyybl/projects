import pandas as pd

df = pd.read_csv('world-happiness-report.csv')
df2 = pd.read_csv('world-happiness-report-2021.csv')

print(df.info())
print(df.head())
