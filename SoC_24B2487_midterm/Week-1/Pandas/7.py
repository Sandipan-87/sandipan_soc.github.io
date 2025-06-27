import pandas as pd
import re
poky=pd.read_csv('Pandas/pokemon_data.csv')
print(poky.loc[poky['Type 1'].str.contains('fire|grass' , flags=re.I , regex=True)])
print(poky.loc[poky['Name'].str.contains('^pi[a-z]*' , flags=re.I , regex=True)])
poky.loc[poky['Type 1']=='Fire' , 'Type 1']= 'Flamer'
poky=poky.iloc[:,6:]
print(poky)