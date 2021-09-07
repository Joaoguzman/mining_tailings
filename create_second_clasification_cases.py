import pandas as pd

df_clasificated = pd.read_excel("predictions.xlsx")
df_clasificated['prediction'] = df_clasificated['prediction'].map({0: 1.0, 1: 2.0})
print(df_clasificated)
list_classified = df_clasificated.prediction.to_list()
print(list_classified[:10])

df_total_db = pd.read_excel("primera_tanda_clasificacion.xlsx", index=False)
del df_total_db['Unnamed: 0']
del df_total_db['Nombre_persona']
print(df_total_db.columns)
idx = 19  
df_total_db.insert(loc=idx, column='prediction', value=list_classified)
print(df_total_db.columns)
# print(df_total_db[["categoria_paper", "prediction"]].head(n=50))

df_total_db.to_excel("resultados_prediccion_modelo_entrenado_segunda_tanda_clasificacion.xlsx" )
