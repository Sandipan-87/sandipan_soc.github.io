import pandas as pd
for poky in pd.read_csv('Pandas/pokemon_data.csv' , chunksize=50 ) :
    print('NEW CHUNK')
    print(poky)
#dealing with large dataset
 