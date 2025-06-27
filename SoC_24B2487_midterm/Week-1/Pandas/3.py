import pandas as pd
poky=pd.read_csv('Pandas/pokemon_data.csv')
print(poky.describe())
print(poky.sort_values('Name', ascending=False))
print(poky.sort_values(['Type 1', 'HP'] , ascending=[1,0]))