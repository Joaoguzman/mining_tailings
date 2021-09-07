import pandas as pd
import random

data = pd.read_excel("database_relaves_final.xlsx")

lista = data["Abstract"].tolist()
print(len(data))
datos_columna= []
for i in range(5):
    datos_columna.append(random.choice(lista))

df = pd.DataFrame({'col':datos_columna})
print (df)

# df.to_excel("5_casos.xlsx")