import pandas as pd

df = pd.read_excel("cleaned_database.xlsx")
df=df.sample(frac=1)
print(df.columns)
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1]'])
df.to_excel("cleaned_database_shuffled.xlsx")