import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import Data
df = pd.read_excel("resultados_prediccion_modelo_entrenado_segunda_tanda_clasificacion.xlsx")
df["prediction"].replace({1.0: "Retrospectivo", 2.0: "Prospectivo"}, inplace=True)

prospectivo=df.loc[df['prediction'] == "Prospectivo"]
prospectivo=prospectivo.groupby('Year').count()
retrospectivo=df.loc[df['prediction'] == "Retrospectivo"]
retrospectivo=retrospectivo.groupby('Year').count()

fig, ax = plt.subplots()

print(prospectivo.index.values.tolist(), prospectivo.Authors.to_numpy())
# print(prospectivo.prediction.to_numpy(), prospectivo.Year.to_numpy())
# print(prospectivo.groupby('Year').count())
print(prospectivo.prediction)
print(retrospectivo.prediction)
print(retrospectivo.columns)

