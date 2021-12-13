import pandas as pd
import time
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder as le
import matplotlib.pyplot as plt

#   COLLECTION
df = pd.read_csv('heart.csv')
data = df.loc[:, ['Age', 'Sex', 'RestingBP', 'Cholesterol', 'HeartDisease']]

#   PREPROCESSING
info = data.describe()
info_rows = ['count', 'min', 'max']
print(info)
print(info.loc[info_rows, :], '\n')

min_age = info.loc['min', 'Age']
max_age = info.loc['max', 'Age']
missing_vals = data[data['Cholesterol'] == 0]

for missing_val in missing_vals.index.values:
    data.drop(missing_val, axis=0, inplace=True)

info = data.describe()
count = data.describe().loc['count', 'Age']
print(info.loc[info_rows, :], '\n')

print(f'There are {count} participants.')
print(f'Ages range from {min_age} to {max_age}. \n')

#   MINING PRINT CORRELATION ANALYSIS HERE
print(data.corr())
#   ANALYSIS PERFORM UNIVARIANT, COVARIANT, AND MULTIVARIANT UP TO MULTI REGRESSION
print(data.head())
print(data['Age'].value_counts())
