import pandas as pd

import nlpaug.augmenter.char as nac
import nlpaug.augmenter.word as naw
import nlpaug.augmenter.sentence as nas
import nlpaug.flow as nafc


df = pd.read_excel("primera_tanda_clasificacion.xlsx")

prediction = []
for i in range(len(df)):
    prediction.append(1)

df = df[["Abstract"]]

idx = 0   
df.insert(loc=idx, column='categoria_paper', value=prediction)

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

# print(df.Abstract[0])

import numpy as np
unique, counts = np.unique(df.categoria_paper, return_counts=True)

print(np.asarray((unique, counts)).T)

df_augmented_cases = pd.DataFrame(columns=["categoria_paper", "Abstract"])
for index, row in df.iterrows():
    if row["categoria_paper"] == True:
        # print(row["Abstract"])
        aug = naw.SynonymAug(aug_src='wordnet')
        augmented_synonymous = aug.augment(row["Abstract"])
        aug = naw.RandomWordAug()
        augmented_delete = aug.augment(augmented_synonymous)
        abstract=augmented_delete
        abstract=nltk.tokenize.word_tokenize(abstract)
        abstract  = ' '.join(abstract)
        df_augmented_cases.loc[len(df_augmented_cases)] = [row["categoria_paper"], abstract]


for index, row in df.iterrows():
    if row["categoria_paper"] == True:
        df_augmented_cases.loc[len(df_augmented_cases)] = [row["categoria_paper"], row["Abstract"]]


df.to_csv('relaves_clasification_total_database.csv', index=False, header=False)