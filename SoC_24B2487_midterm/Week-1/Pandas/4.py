import pandas as pd
poky=pd.read_csv('Pandas/pokemon_data.csv')
#poky['Total']= poky['Speed']+poky['HP'] similarly,
poky['Total']=poky.iloc[: , 4:10].sum(axis=1)
#print(poky.head(7))
#poky = poky.drop(columns='Total')
print(poky.head(7))