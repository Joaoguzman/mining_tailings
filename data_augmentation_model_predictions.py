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

# df_total_db.to_excel("resultados_segundo_modelo_entrenado_primera_tanda_clasificacion.xlsx" )

df_retrospectivo = df_total_db[df_total_db.prediction == 2.0]
# df_total_db = df_total_db[df_total_db.categoria_paper != 99]
# df_total_db = df_total_db[df_total_db.categoria_paper != 98]
# df_total_db = df_total_db[df_total_db.categoria_paper != 1]
# df_total_db = df_total_db[df_total_db.categoria_paper != 2]
print(len(df_retrospectivo))

import pandas as pd

import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc


df = pd.read_excel("segunda_tanda_clasificacion.xlsx")
df = df[df.categoria_paper.notnull()]
df = df[df.categoria_paper != 99]
df = df[df.categoria_paper != 98]

df = df[["categoria_paper", "Abstract"]]

# df = df.categoria_paper.replace([1.0, 2.0], [0, 1], inplace=True)
df['categoria_paper'] = df['categoria_paper'].map({1.0: 0, 2.0: 1})


import nltk
stop_words=nltk.corpus.stopwords.words("english")
for index, row in df.iterrows():
    abstract = row["Abstract"]
    abstract = abstract.encode('ascii', 'ignore').decode()
    # abstract=abstract.lower()
    abstract=nltk.tokenize.word_tokenize(abstract)
    abstract= [x for x in abstract if x not in stop_words]
    for iteration, item in enumerate(abstract):
        lemma=nltk.stem.WordNetLemmatizer().lemmatize(item, 'v')
        abstract[iteration] = lemma
    abstract  = ' '.join(abstract)
    # print(abstract)
    df['Abstract'][index] = abstract

import numpy as np
unique, counts = np.unique(df.categoria_paper, return_counts=True)

print(np.asarray((unique, counts)).T)

df_augmented_cases = pd.DataFrame(columns=["categoria_paper", "Abstract"])
for index, row in df.iterrows():
    if row["categoria_paper"] == 0 or 1:
        # print(row["Abstract"])
        aug = naw.SynonymAug(aug_src='wordnet')
        augmented_synonymous = aug.augment(row["Abstract"])
        aug = naw.RandomWordAug()
        augmented_delete = aug.augment(augmented_synonymous)
        abstract=augmented_delete
        abstract=nltk.tokenize.word_tokenize(abstract)
        abstract  = ' '.join(abstract)
        df_augmented_cases.loc[len(df_augmented_cases)] = [row["categoria_paper"], abstract]


from collections import Counter
c = Counter( df_augmented_cases.categoria_paper.to_list())
print( c.items() )
c = Counter( df.categoria_paper.to_list())
print( c.items() )

# df.to_csv('relaves_clasification.csv', index=False, header=False)
# df_augmented_cases.to_csv('relaves_clasification_augmented_cases.csv', index=False, header=False)