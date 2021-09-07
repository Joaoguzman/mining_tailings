import pandas as pd

df = pd.read_excel("cleaned_database_shuffled.xlsx")
del df['Unnamed: 0']
del df['Unnamed: 0.1']
del df['Unnamed: 0.1.1']
del df['Unnamed: 0.1.1.1']


idx = 16
new_col = []  # can be a list, a Series, an array or a scalar   

for i in range(len(df)):
    if i < 50:
        new_col.append("Fernando")
    elif i > 49 and i < 100:
        new_col.append("Joao")
    elif i > 99 and i < 150:
        new_col.append("Iván")
    elif i > 149 and i < 200:
        new_col.append("Joaquín")
    elif i > 199 and i < 250:
        new_col.append("Fernando")
    elif i > 249 and i < 300:
        new_col.append("Joao")
    elif i > 299 and i < 350:
        new_col.append("Iván")
    elif i > 349 and i < 400:
        new_col.append("Joaquín")
    else:
        new_col.append("")
df.insert(loc=idx, column='Nombre_persona', value=new_col)

idx = 18
new_col = []  # can be a list, a Series, an array or a scalar   
for i in range(len(df)):
    new_col.append("")
df.insert(loc=idx, column='categoria_paper', value=new_col)

idx = 19
new_col = []  # can be a list, a Series, an array or a scalar   
for i in range(len(df)):
    new_col.append("")
df.insert(loc=idx, column='comentarios_cualitativos', value=new_col)

print(df.columns)
print(len(df))

df.to_excel("primera_tanda_clasificacion.xlsx")