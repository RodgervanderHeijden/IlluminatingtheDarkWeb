import pandas as pd

df = pd.read_csv(r'../data/raw/product_20210517.csv')
df.drop(df.columns[0], axis=1, inplace=True)

# The price in $s is captured as a string, containing both decimal points and commas. Here we clean that to a float
df['price'] = [round(float(x)) if len(x) <= 6 else float(x[:-3].replace(",", "")) for x in df['price in $']]
# to do: add country of origin to the vendor dataset. Can be extracted from drugs dataset.
# vendor can have multiple shipping from locations --> unable to trace exact country of origin
df.to_csv('../data/cleaned/product_20210517.csv', index=False)
