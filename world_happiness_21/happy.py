import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#   figure object
ax_bar = plt.axes()

#   collect
df = pd.read_csv('world-happiness-report-2021.csv')
columns = ['Country name', 'Ladder score', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices',
           'Generosity', 'Perceptions of corruption']
data = df[columns]
print(f'Rows: {data.shape[0]} | Columns: {data.shape[1]}')

#   EDA
df[columns].corr().to_csv('corrs.csv')
x = data.iloc[:, 3:4].values
y = data.iloc[:, 2:3].values

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=.8)

#   linear reg - social support predicting life expectancy score
reg = LinearRegression()
reg.fit(x_train, y_train)

ax_scatter = plt.axes()
ax_scatter.scatter(x_test, y_test, color='green')
ax_scatter.plot(x_test, reg.predict(x_test), color='black')
plt.show()

#   happiest countries according to ladder score
top_ladder = df[columns].sort_values(by='Ladder score', ascending=False).head(20)

countries_and_score = top_ladder.loc[:, ['Country name', 'Ladder score']]
x_bar = countries_and_score.iloc[:, 0].values
y_bar = countries_and_score.iloc[:, 1].values

# ax_bar.barh(x_bar, y_bar)
# ax_bar.set_xlim(6.8, 7.9)
# ax_bar.set_xlabel('Ladder Score')
# ax_bar.set_ylabel('Country')
# plt.show()
#
