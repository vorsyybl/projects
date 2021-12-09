import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw = pd.read_csv('mw_90.csv')
raw.drop(['Unnamed: 0', 'Unnamed: 15', 'Unnamed: 1'], axis=1, inplace=True)
raw.rename(columns={'Game': 'title'}, inplace=True)
raw.drop([0, 1, 5, 6, 8, 9, 11, 12, 13], axis=0, inplace=True)

top10 = raw.loc[:, ['title', 'Watch time', 'Average viewers', 'Views gained', 'Followers gained']].head(10)

top10.plot.barh(x='title', y='Watch time')
plt.show()

top10.to_csv('top10_90.csv')

