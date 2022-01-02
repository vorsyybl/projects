import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import time as t

#   collect
df = pd.read_csv('world-happiness-report-2021.csv')
columns = ['Country name', 'Ladder score', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices',
           'Generosity', 'Perceptions of corruption']
data = df[columns]
print(f'Rows: {data.shape[0]} | Columns: {data.shape[1]}')

#   EDA
df[columns].corr().to_csv('corrs.csv')
y = data.iloc[:, 3:4].values
x = data.iloc[:, 2:3].values

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=.8)

#   linear reg - social support predicting life expectancy score
reg = LinearRegression()
print(f'x min: {x.min()} \n x max: {x.max()} \n y min: {y.min()} \n y max: {y.max()}')
reg.fit(x, y)
y_pred = reg.predict(x)

#   figure object
ax = plt.axes()
ax.scatter(x, y, color='red')
ax.plot(x, y_pred, color='yellow')
ax.set_title('Original Data: Social Support to Predict Life Expectancy')
ax.set_xlabel('Social Support Score')
ax.set_ylabel('Life Expectancy Score')
ax.set_facecolor('teal')
plt.show()
t.sleep(3)

#   figure object 2
ax1 = plt.axes()
ax1.scatter(x_test, y_test, color='red')
ax1.plot(x_test, reg.predict(x_test), color='yellow')
ax.set_title('Test Data: Social Support to Predict Life Expectancy')
ax1.set_xlabel('Social Support Score')
ax1.set_ylabel('Life Expectancy Score')
ax1.set_facecolor('teal')
plt.show()
t.sleep(3)

#   happiest countries according to ladder score
top_ladder = df[columns].sort_values(by='Ladder score', ascending=False).head(20)

countries_and_score = top_ladder.loc[:, ['Country name', 'Ladder score']]
x_bar = countries_and_score.iloc[:, 0].values
y_bar = countries_and_score.iloc[:, 1].values

ax3 = plt.axes()
ax3.barh(x_bar, y_bar, color='yellow')
ax3.set_xlim(6.8, 7.9)
ax3.set_title('Top 20 Happiest Countries as a Function of Ladder Score')
ax3.set_xlabel('Ladder Score')
ax3.set_ylabel('Country')
ax3.set_facecolor('green')
plt.show()

