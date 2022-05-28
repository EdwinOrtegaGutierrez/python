import pandas as pd

dict_ = {'a':[11, 21, 31], 'b':[12, 22, 32]}

df = pd.DataFrame(dict_)

print(df.head()) # Ordena los valores
print(df.mean()) # Saca el promedio