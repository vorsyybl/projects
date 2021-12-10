import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

df = pd.read_csv('heart.csv')

data = df.loc[:, ['Age', 'Sex', 'RestingBP', 'Cholesterol', 'HeartDisease']]
info = data.describe()

#   Possible missing values, impossible to have 0 resting BP, and/or 0 chole?

min_age = info.loc['min', 'Age']
max_age = info.loc['max', 'Age']
max_chol = info.loc['max', 'Cholesterol']
min_chol = info.loc['min', 'Cholesterol']

print(info)

print(f'Ages range from {min_age} to {max_age}.')
print(f'Cholesterol blood ratio range from {min_chol} to {max_chol}.')

# find and ommit missing values
