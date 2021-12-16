import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np

#   COLLECTION
df = pd.read_csv('heart.csv')
data = df.loc[:, ['Age', 'Sex', 'RestingBP', 'Cholesterol', 'HeartDisease']]

#   REMOVING OUTLIERS
rbp_out = data[(data['RestingBP'] > 170) | (data['RestingBP'] < 90)].index.values
chol_out = data[(data['Cholesterol'] > 408) | (data['Cholesterol'] < 85)].index.values
outliers = (set(rbp_out).union(set(chol_out)))
for row in outliers:
    data.drop(row, axis=0, inplace=True)

le = LabelEncoder()
data2 = data
data2['Sex'] = le.fit_transform(data2['Sex'])

print(data2.columns.values)
# print(data2.dtypes)
# print(data2.corr())

x = data2.iloc[:, :-1].values
y = data2.iloc[:, -1].values

print(x, '\n', y, '\n')
print(x.shape, '\n', y.shape)
print(type(x), '\n', type(y))

# ax = plt.axes()
# ax.scatter(x, y)
# ax.show()
