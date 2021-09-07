from os import remove
import pandas as pd
import nltk
data = pd.read_excel("database_relaves_final_todas_columnas.xlsx")

syn_mineral = ['mine','mineral', 'ore']
syn_dam = ['dam', 'dike', 'dyke']
syn_tailing = ['shadow', 'tail']


for index, row in data.iterrows():
    abstract = row["Abstract"]
    abstract=abstract.lower()
    if "tailing effects" in abstract:
        data=data.drop(index)
        continue
    abstract=nltk.tokenize.word_tokenize(abstract)
    for iteration, item in enumerate(abstract):
        lemma=nltk.stem.WordNetLemmatizer().lemmatize(item, 'v')
        abstract[iteration] = lemma
    # if syn_dam and syn_tailing not in abstract or syn_mineral and syn_tailing not in abstract:
    boolean_tailing=any(item in syn_tailing for item in abstract)
    boolean_mineral=any(item in syn_mineral for item in abstract)
    boolean_dam=any(item in syn_dam for item in abstract)
    remove_1 = boolean_dam and boolean_tailing
    remove_2 = boolean_mineral and boolean_tailing
    remove = remove_1 or remove_2
    if remove == False:
        data=data.drop(index)
    
print(data)

import collections
counter=collections.Counter(data['Source title'].tolist())
counter={k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}

common_journals = {}
for i in range(1, 11):
    common_journals[list(counter.keys())[-i]] = list(counter.values())[-i] 

df_frecuency_table = pd.DataFrame(
    {
        "journal" : list(counter.keys())[::-1],
        "frecuency" : list(counter.values())[::-1]
    }
    )
print(df_frecuency_table)
df_frecuency_table.to_excel("Journal_frecuency.xlsx")
data.to_excel("cleaned_database.xlsx")