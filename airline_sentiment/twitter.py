import pandas as pd
import matplotlib.pyplot as plt

#   COLLECTION
df = pd.read_csv('Tweets.csv')

#   ABSTRACT
columns = df.columns.values
info = df.info()
description = df.describe()
print(columns, '\n',  info, '\n', description)

#   WRANGLING
sentiment = df.loc[:, ['airline', 'airline_sentiment']]
sentiment_proportions = sentiment['airline_sentiment'].value_counts()
print(sentiment)
print(sentiment_proportions)

ax = plt.axes()
ax.pie(sentiment_proportions, labels=['negative', 'neutral', 'positive'])
plt.show()
