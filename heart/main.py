import pandas as pd
import time
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer as ct
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder as le
import matplotlib.pyplot as plt
import numpy as np

#   COLLECTION
df = pd.read_csv('heart.csv')
data = df.loc[:, ['Age', 'Sex', 'RestingBP', 'Cholesterol', 'HeartDisease']]

#   PREPROCESSING
info = data.describe()
info_rows = ['count', 'min', 'max']
print(info)
print(info.loc[info_rows, :], '\n')

empty_vals = data[data['Cholesterol'] == 0]

for missing_val in empty_vals.index.values:
    data.drop(missing_val, axis=0, inplace=True)

info = data.describe()
count = data.describe().loc['count', 'Age']
print(info.loc[info_rows, :], '\n')

#   EDA
print(f'There are {count} participants.')
sex_counts = data['Sex'].value_counts()
counts = [sex_counts[0], sex_counts[1]]
gender = [sex_counts.index.values[0], sex_counts.index.values[1]]

plt.bar(gender, counts)
plt.show()

plt.hist(x=data['Age'], bins=10)
plt.show()

#   MINING PRINT CORRELATION ANALYSIS HERE
# print(data.corr())
#   ANALYSIS PERFORM UNIVARIANT, COVARIANT, AND MULTIVARIANT UP TO MULTI REGRESSION

