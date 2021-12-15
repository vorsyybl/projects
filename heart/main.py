import pandas as pd
import time
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

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

rbp_out = data[(data['RestingBP'] > 170) | (data['RestingBP'] < 90)].index.values
chol_out = data['Cholesterol'][(data['Cholesterol'] > 408) | (data['Cholesterol'] < 85)].index.values

for row in rbp_out:
    data.drop(row, axis=0, inplace=True)
for row in chol_out:
    try:
        data.drop(row, axis=0, inplace=True)
    except:
        print(f'{row} already removed....')
        time.sleep(1)
        continue

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
ax.boxplot([data['RestingBP'], data['Cholesterol']], labels=['RestingBP', 'Cholesterol'])
ax.set_facecolor('grey')
ax.set_ylabel('RestingBP')
plt.show()

#   MINING LOOK FOR RELATIONSHIPS COVARIANT, AND MULTIVARIANT UP TO MULTI REGRESSION
corrs = data.corr()
print(data.shape)
print(data.describe())
print(corrs)

#  
