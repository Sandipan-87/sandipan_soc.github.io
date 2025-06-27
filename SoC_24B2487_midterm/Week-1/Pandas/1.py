import pandas as pd
poky = pd.read_csv('Pandas/pokemon_data.csv')
print(poky.head(10))
#similarly poky.tail()
#for reading excel , poky.read_excel('')
#for txt, poky.read_csv('', delimiter='\t')