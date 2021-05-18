import pandas as pd
from my_pandas_folder import *

def extract_elder(my_file_with_elder):

    df = pd.read_csv(my_file_with_elder, index_col=None, header=0, sep=',', low_memory=False)
    df['date_year'] = df['date de naissance'].str[-4:]
    df['date_year'] = df['date_year'].astype(int)
    limit = 1956
    df = df.drop(df[(df['date_year'] > limit)].index)
    df.to_csv(my_pandas_folder+'/DraftElder.csv', encoding='utf8', index=False)
