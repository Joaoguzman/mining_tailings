import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Import Data
df = pd.read_excel("resultados_prediccion_modelo_entrenado_segunda_tanda_clasificacion.xlsx")

df["prediction"].replace({1.0: "Retrospectivo", 2.0: "Prospectivo"}, inplace=True)

# Prepare data
x_var = 'Year'
groupby_var = 'prediction'
df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
vals = [df[x_var].values.tolist() for i, df in df_agg]

# Draw
plt.figure(figsize=(16,9), dpi= 80)
colors = [plt.cm.Accent(i/float(len(vals)-1)) for i in range(len(vals))]
n, bins, patches = plt.hist(vals, df[x_var].unique().__len__(), stacked=True, density=False, color=colors[:len(vals)])

# Decoration
plt.legend({group:col for group, col in zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
plt.title(f"Evolución en la perspectiva de estudio de los relaves por año.", fontsize=22)
plt.xlabel("Año")
plt.ylabel("Frecuencia")
plt.ylim(0, 1200)
plt.xticks(ticks=bins, labels=np.unique(df[x_var]).tolist(), rotation=90, horizontalalignment='left')
plt.show()

# pip install squarify
import squarify 
import ast
import numpy as np


print(len(df))
# Import Data
for index, row in df.iterrows():
    if row["Field"][0] == "[":
        print(row["Field"])
        list_fields = ast.literal_eval(row["Field"])
        for i in list_fields:
            df.loc[len(df)] = list(np.random.randint(10, size=len(df.columns)-4)) + [i] + list(np.random.randint(10, size=3))
print(len(df))
for index, row in df.iterrows():
    if isinstance(row["Field"], int):
        continue
    characteristic=row["Field"][0]
    if characteristic == "[":
        df = df.drop(index)

print(len(df))


df_raw = df

# Prepare Data
df = df_raw.groupby('Field').size().reset_index(name='counts')
labels = df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
sizes = df['counts'].values.tolist()
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

# Draw Plot
plt.figure(figsize=(12,8), dpi= 80)
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

# Decorate
plt.title('Campos desde los que se aborda el estudio de los relaves')
plt.axis('off')
plt.show()