import pandas as pd
import matplotlib.pyplot as plt

#   figure object
ax = plt.axes()

#   collect
df = pd.read_csv('world-happiness-report-2021.csv')
columns = ['Country name', 'Ladder score', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices',
           'Generosity', 'Perceptions of corruption']

#   happiest countries according to ladder score
top_ladder = df[columns].sort_values(by='Ladder score', ascending=False).head(20)
countries_and_score = top_ladder.loc[:, ['Country name', 'Ladder score']]
x_bar = countries_and_score.iloc[:, 0].values
y_bar = countries_and_score.iloc[:, 1].values

print(f'Rows:{top_ladder.shape[0]} | Columns: {top_ladder.shape[1]}')
print(top_ladder.describe())
print(top_ladder.info)

ax.barh(x_bar, y_bar)
ax.set_xlim(6.8, 7.9)
ax.set_xlabel('Ladder Score')
ax.set_ylabel('Country')
plt.show()

