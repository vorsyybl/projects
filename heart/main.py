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

empty_vals = data[data['Cholesterol'] == 0]

for missing_val in empty_vals.index.values:
    data.drop(missing_val, axis=0, inplace=True)

#   EDA
info = data.describe()
count = data.shape[0]
sex_counts = data['Sex'].value_counts()
counts = [sex_counts[0], sex_counts[1]]
gender = [sex_counts.index.values[0], sex_counts.index.values[1]]

ax = plt.axes()
ax.boxplot([data['RestingBP'], data['Cholesterol']], labels=['RestingBP', 'Cholesterol'])
ax.set_facecolor('grey')
ax.set_ylabel('??????????????')
plt.show()

print(f'There are {count} participants, {counts[0]} Male, {counts[1]} female.')
time.sleep(5)

ax = plt.axes()
ax.set_facecolor('grey')
ax.bar(gender, counts, color='orange', edgecolor='black', linewidth=3)
ax.set_title('Gender Distribution')
ax.set_xlabel('GENDER')
ax.set_ylabel('TOTAL')
plt.show(block=False)
plt.pause(8)
plt.close()

print('Participants are mostly between 50 and 60 years old.')
time.sleep(5)

ax = plt.axes()
ax.set_facecolor('grey')
ax.hist(x=data['Age'], bins=10, color='orange', edgecolor='black', linewidth=3)
ax.set_title('Age Distribution')
ax.set_xlabel('AGE')
ax.set_ylabel('TOTAL')
plt.show(block=False)
plt.pause(8)
plt.close()

#   MINING LOOK FOR RELATIONSHIPS
corrs = data.corr()

#  COVARIANT, AND MULTIVARIANT UP TO MULTI REGRESSION
