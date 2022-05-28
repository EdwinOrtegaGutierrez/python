import pandas as pd

df = pd.DataFrame({'a':[11, 21, 31], 'b':[21, 22, 23]})

print(df['a'])

print("\n")

print(df.head(3))

print(df.iloc[0, 1])