import pandas as pd

data = pd.read_excel("base_datos_relaves_totales.xlsx")

def limit_information_required(columns_list, df):
    data_filtered = df[columns_list]
    data_filtered.to_excel("base_datos_filtrados.xlsx")
    return data_filtered

def convine_same_paper_different_feald(field_column, abstract_column, df): # len = 15259, 15153
    count = 0
    list_indexes = []
    for index, row in df.iterrows():
        sub_df = df.loc[df[abstract_column] == row[abstract_column]]
        if len(sub_df.index) > 1:
            list_indexes.append([sub_df.index.values.tolist(), sub_df[field_column].tolist()])
            count += 1
    print(count)
    textfile = open("lista_mismo_estudio_varios_campos.txt", "w")
    textfile.write(str(list_indexes))
    textfile.close()


import ast

def read_file_with_list(path):
    f = open(path, "r")
    list_download = ast.literal_eval(f.read())
    return list_download

def eliminate_duplicate_elements_list(list_with_duplicates):
    list_already_processed = []
    list_fields = []
    for i in range(len(list_with_duplicates)):
        if list_with_duplicates[i][0] in list_already_processed:
            continue
        index = list_with_duplicates[i][0]
        Fields = list_with_duplicates[i][1]
        list_already_processed.append(list_with_duplicates[i][0])
        list_fields.append(list_with_duplicates[i][1])
    return list_already_processed, list_fields

def eliminate_duplicate_rows(df, index_list, field_list):
    for i in range(len(index_list)):
        i_without_first_element = index_list[i][1:]
        print(field_list[i])
        df.at[index_list[i][0], 'Field'] = field_list[i]
        for repeated in range(len(i_without_first_element)):
            repeated_index = repeated + 1
            df = df.drop(index_list[i][repeated_index])
    print(len(df.index.values.tolist()))
    df.to_excel("database_relaves_final" + ".xlsx")

needed_columns = [
    "Title",
    "Abstract",
    "Year",
    "Author Keywords",
    "Index Keywords",
    "Authors",
    "Authors with affiliations",
    "Field"
    ]

def run():
    df_filtered = limit_information_required(needed_columns, data)
    
    
    list_similar_rows = read_file_with_list("lista_mismo_estudio_varios_campos.txt")
    list_index, list_fields=eliminate_duplicate_elements_list(list_similar_rows)
    eliminate_duplicate_rows(df_filtered, list_index, list_fields)


if __name__ == "__main__":
    run()