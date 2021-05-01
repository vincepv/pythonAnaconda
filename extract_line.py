import pandas as pd
def extract_line(my_file,column_name,value_to_extract):
    """
    :param my_file: name of the file to process
    :param column_name: name of the column where extract is process
    :param value_to_extract: value to use for extract in the given column
    :return a new file with only lines matching param
    Ex. with 2 param
    df_extract = df.loc[(df[column_name] == value_to_extract) & (df[column_name_2] == value_to_extract_2) ]
    """
    df = pd.read_csv(my_file, low_memory=False)
    df_extract = df.loc[(df[column_name] == value_to_extract)]
    df_extract.to_csv('/Users/VPV/Desktop/pandas/extract.csv', header=True, index=False, encoding="utf8")