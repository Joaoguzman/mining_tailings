import pandas as pd

x = pd.read_excel("resultados_prediccion_modelo_entrenado_primera_tanda_clasificacion.xlsx")

# print(x.columns)
print(x.groupby('categoria_paper').count())