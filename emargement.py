import pandas as pd
from my_pandas_folder import *

def emargement(my_file,keyword1,keyword2,empty_t1,empty_t2):
    """
    my_file = file to process
    keyword1 = use to fill column t1
    keyword1 = use to fill column t2

    """
    df = pd.read_csv(my_file, low_memory=False, sep=",",encoding="utf-8")

    if 't1' in df:
        df['t1'] = df['t1'].fillna(empty_t1)
        df['t1'] = df['t1'].astype(str)
        df['t1'] = df['t1'].replace(['x','X','oui'],keyword1)
        

    if 't2' in df:
        df['t2'] = df['t2'].fillna(empty_t2)
        df['t2'] = df['t2'].astype(str)
        df['t2'] = df['t2'].replace(['x','X','oui'],keyword2)

    if  't1' and 't2' in df:   
        df['emargement'] = df['t1'] + "," + df['t2']

    df.to_csv(my_pandas_folder+'/DraftEmarg.csv', header=True, index=False, encoding="utf8")