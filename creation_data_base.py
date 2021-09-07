import pandas as pd
import os

def convine_data(directory, columns, database_name):
    df = pd.DataFrame(columns=columns)
    for filename in os.listdir(directory):
        data = pd.read_csv(
            directory + filename, 
            encoding="utf-8", 
            error_bad_lines=False
            )
        data["Field"] = filename[:4]
        df = pd.concat(
            [df, data], 
            ignore_index=True
            )
    df.to_excel(database_name + ".xlsx")


columns_tailing = ['Authors', 'Author(s) ID', 'Title', 'Year', 'Source title', 'Volume',
       'Issue', 'Art. No.', 'Page start', 'Page end', 'Page count', 'Cited by',
       'DOI', 'Link', 'Affiliations', 'Authors with affiliations', 'Abstract',
       'Author Keywords', 'Index Keywords', 'Molecular Sequence Numbers',
       'Chemicals/CAS', 'Tradenames', 'Manufacturers', 'Funding Details',
       'Funding Text 1', 'References', 'Correspondence Address', 'Editors',
       'Sponsors', 'Publisher', 'Conference name', 'Conference date',
       'Conference location', 'Conference code', 'ISSN', 'ISBN', 'CODEN',
       'PubMed ID', 'Language of Original Document',
       'Abbreviated Source Title', 'Document Type', 'Publication Stage',
       'Open Access', 'Source', 'EID', 'Field']

def run():
    convine_data("C:/Users/joaqu/OneDrive/Documentos/drive/relaves/raw_data/", columns_tailing, database_name = "base_datos_relaves_totales")

if __name__ == "__main__":
    run()