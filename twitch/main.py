import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# WHAT ARE THE MOST POPULAR GAMES BEING WATCHED WITHIN LAST 3 MONTHS??
# (HOPEFULLY THE ANSWER WILL RESULT IN A LARGER AUDIENCE...)

raw = pd.read_csv('mw_90.csv')
print('File read successfully...')

print(raw.columns.values)

raw.drop(['Unnamed: 0', 'Unnamed: 15'], axis=1, inplace=True)
raw.rename(columns={'Unnamed: 1': 'ID'}, inplace=True)

new = raw.loc[:, ['Game', 'Watch time', 'Average viewers', 'Views gained', 'Followers gained']]
new.set_index('Game', inplace=True)
new.drop(['Just Chatting', 'Minecraft', 'Apex Legends', 'Fortnite', 'New World'], axis=0, inplace=True)

new.head(10).to_csv('top10_90.csv')
print('New created successfully...')
