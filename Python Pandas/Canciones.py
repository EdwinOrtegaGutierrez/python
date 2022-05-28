import pandas as pd

df = pd.DataFrame({'Artista':["Caifanes", "Ghost", "The devil makes tree"], 
                    'Genero':["Rock en espanol", "Rock", "Blues"],
                    'Cancion':["Afuera", "Cirice", "Old number seven"]})

print(df.head(3))