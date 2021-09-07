import pandas as pd
import os


df_column_names = pd.read_excel("Joaquín"+"_2_tanda_clasificacion.xlsx", index_col=0)
df_second_clasification = pd.DataFrame(columns=df_column_names.columns)
print(df_second_clasification.columns)
clasificadores=["Fernando", "Iván", "Joao", "Joaquín"]
for i, value in enumerate(clasificadores):
    if os.path.exists(value + "_2_tanda_clasificacion.xlsx"):
        print(value)
        df = pd.read_excel(value+"_2_tanda_clasificacion.xlsx", index_col=0)
        df_second_clasification = pd.concat([df_second_clasification, df])

print(df_second_clasification.head())
print(len(df_second_clasification))
df_first_clasification = pd.read_excel("primera_tanda_clasificacion.xlsx", index_col=0)
print(len(df_first_clasification))
df_first_clasification=df_first_clasification.drop(df_second_clasification.index)
print(len(df_first_clasification))

df_second_clasification = pd.concat([df_first_clasification, df_second_clasification])
print(len(df_second_clasification))
print(len(df_second_clasification.index.unique()))

df_second_clasification = df_second_clasification[df_second_clasification.categoria_paper.notnull()]

print(set(df_second_clasification.categoria_paper.to_list()))

from collections import Counter
c = Counter(df_second_clasification.categoria_paper.to_list())
print(c.items())

df_second_clasification.to_excel("segunda_tanda_clasificacion.xlsx")