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
num_rows = data.shape[0]

#   LOCATE OUTLIERS USING A BOXPLOT
ax = plt.axes()
ax.boxplot([data['RestingBP'], data['Cholesterol']], labels=['RestingBP', 'Cholesterol'])
ax.set_facecolor('grey')
ax.set_ylabel('VALUE')
plt.show()

#   REMOVING OUTLIERS
rbp_out = data[(data['RestingBP'] > 170) | (data['RestingBP'] < 90)].index.values
chol_out = data[(data['Cholesterol'] > 408) | (data['Cholesterol'] < 85)].index.values
outliers = (set(rbp_out).union(set(chol_out)))
for row in outliers:
    data.drop(row, axis=0, inplace=True)

num_rows = data.shape[0]
sex_counts = data['Sex'].value_counts()
counts = [sex_counts[0], sex_counts[1]]
gender = [sex_counts.index.values[0], sex_counts.index.values[1]]

#   EDA
print(f'There are {num_rows} participants, {counts[0]} Male, {counts[1]} female.')
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

#   MINING LOOK FOR RELATIONSHIPS COVARIANT, AND MULTIVARIANT UP TO MULTI REGRESSION
corrs = data.corr()
print(corrs)

#
