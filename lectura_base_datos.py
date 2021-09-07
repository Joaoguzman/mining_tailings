import pandas as pd
import ast # este paquete permite interpretar un string como de manera literal, en este caso 
import numpy as np

# Import Data
df = pd.read_excel("resultados_prediccion_modelo_entrenado_segunda_tanda_clasificacion.xlsx")

for index, row in df.iterrows():
    if row["Field"][0] == "[":
        print(row["Field"])
        df.at[index, 'Field'] = ast.literal_eval(row["Field"])