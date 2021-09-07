from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt

path_data = "resultados_prediccion_modelo_entrenado_segunda_tanda_clasificacion.xlsx"
df = pd.read_excel(path_data)
print(df.head())
print(df.prediction.head(30))

# print(df.columns)
df_pro=df.loc[df['prediction'] == 2]
df_ret=df.loc[df['prediction'] == 1]# Prospectivo Retrospectivo

print(df_pro["Cited by"])
prospective=df_pro["Cited by"].fillna(0).mean()
retrospective=df_ret["Cited by"].fillna(0).mean()

# descriptive
print(df_pro["Cited by"].fillna(0).describe())
print(df_ret["Cited by"].fillna(0).describe())

fig, ax = plt.subplots()

ax.bar(["Retrospective", "Prospective"], [retrospective, prospective],color='#A4A4A4', align='center')

# ax.set_title("Number of citations for each study perspective")
ax.set_ylabel("Average citations per article")
ax.set_xlabel("Perspective")
# ax.legend()
plt.show()