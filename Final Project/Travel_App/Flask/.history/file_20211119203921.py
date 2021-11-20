import pandas as pd
pd.
df_yelp = pd.read_table('yelp_labelled.txt')
df_imdb = pd.read_table('imdb_labelled.txt')
df_amz = pd.read_table('amazon_cells_labelled.txt')

# Concatenate our Datasets
frames = [df_yelp,df_imdb,df_amz]

# Renaming Column Headers
for colname in frames:
    colname.columns = ["Message","Target"]

# Column names
for colname in frames:
    print(colname.columns)

# Assign a Key to Make it Easier
keys = ['Yelp','IMDB','Amazon']

# Merge or Concat our Datasets
df = pd.concat(frames,keys=keys)