import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#   COLLECTION
df = pd.read_csv('heart.csv')
data = df.loc[:, ['Age', 'Sex', 'RestingBP', 'Cholesterol', 'HeartDisease']]

#   PREPROCESSING
info = data.describe()
print(info, '\n')

min_age = info.loc['min', 'Age']
max_age = info.loc['max', 'Age']
missing_vals = data[data['Cholesterol'] == 0]

for missing_val in missing_vals.index.values:
    data.drop(missing_val, axis=0, inplace=True)

count = data.describe().loc['count', 'Age']

print(f'There are {count} rows.')
print(f'Ages range from {min_age} to {max_age}. \n')

info = data.describe()
print(info, '\n')

#   MINING

