import pandas as pd


def extract_elder(my_file):

    df = pd.read_csv(my_file, index_col=None, header=0, sep=',', low_memory=False)
    df['date_year'] = df['date de naissance'].str[-4:]
    df['date_year'] = df['date_year'].astype(int)
    limit = 1956
    df = df.drop(df[(df['date_year'] > limit)].index)
    df.to_csv('/Users/VPV/Desktop/pandas/DraftElder.csv', encoding='utf8', index=False)
