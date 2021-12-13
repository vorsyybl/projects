import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

#   COLLECTION
df = pd.read_csv('heart.csv')
data = df.loc[:, ['Age', 'Sex', 'RestingBP', 'Cholesterol', 'HeartDisease']]

#   PREPROCESSING
info = df.describe()
print(info, '\n')

min_age = info.loc['min', 'Age']
max_age = info.loc['max', 'Age']
missing_vals = data[data['Cholesterol'] == 0]

for missing_val in missing_vals.index.values:
    data.drop(missing_val, axis=0, inplace=True)

count = data.describe().loc['count', 'Age']

print(f'There are {count} rows.')
print(f'Ages range from {min_age} to {max_age}. \n')
