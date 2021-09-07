import squarify 
import ast
import numpy as np
import pandas as pd

df = pd.read_excel("resultados_prediccion_modelo_entrenado_segunda_tanda_clasificacion.xlsx")

df["prediction"].replace({1.0: "Retrospectivo", 2.0: "Prospectivo"}, inplace=True)

iterations = 0
for index, row in df.iterrows():
    if row["Field"][0] == "[":
        iterations +=1
        # print(row["Field"])
        list_fields = ast.literal_eval(row["Field"])
        list_fields = set(list_fields)
        list_fields = list(list_fields)
        for i in list_fields:
            df.loc[len(df)] = list(df.iloc[index,:49]) + [i] + list(df.iloc[index,50:])
        #     print(list(df.iloc[-1,5:10]))
        # print(df.iloc[-3:,5:10])
print(len(df))
for index, row in df.iterrows():
    if isinstance(row["Field"], int):
        continue
    characteristic=row["Field"][0]
    if characteristic == "[":
        df = df.drop(index)
print(len(df))
print("iterations", iterations)

df.to_excel("fields_separados.xlsx")