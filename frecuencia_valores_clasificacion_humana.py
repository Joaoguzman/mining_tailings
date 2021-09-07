import pandas as pd


# Import Data
df = pd.read_excel("resultados_prediccion_modelo_entrenado_segunda_tanda_clasificacion.xlsx")
df=df.groupby('prediction').count()

print(df)