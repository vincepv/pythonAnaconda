import pandas as pd
from my_pandas_folder import *
# csv utf8 
def merge_on_first_last_date(input1,input2):
    # input1 = electoral file
    df1 = pd.read_csv(input1, low_memory=False)
    df2 = pd.read_csv(input2, low_memory=False)

    # clean file for merge, case sensitive
    df1['prenom'] = df1['prenom'].str.strip()
    df1['nom'] = df1['nom'].str.strip()

    df1['nom'] = df1['nom'].str.capitalize()
    df1['prenom'] = df1['prenom'].str.capitalize()

    df2['prenom'] = df2['prenom'].str.strip()
    df2['nom'] = df2['nom'].str.strip()

    df2['prenom'] = df2['prenom'].str.capitalize()
    df2['nom'] = df2['nom'].str.capitalize()
    
    # create duplicate file to tracks duplicate contact not in merge file
    
    dfdup1 = df1[df1.duplicated(['prenom', 'nom', 'date'], keep=False)]
    dfdup2 = df2[df2.duplicated(['prenom', 'nom', 'date'], keep=False)]
    
    dfdup1.to_csv(my_pandas_folder+'/Duplicate1.csv', encoding='utf8', index=False)
    dfdup2.to_csv(my_pandas_folder+'/Users/VPV/Desktop/pandas/Duplicate2.csv', encoding='utf8', index=False)
    
    # remove duplicate before merge, avoid to merge false data

    df1 = df1.drop_duplicates(subset=['prenom', 'nom', 'date'],keep=False)
    df2 = df2.drop_duplicates(subset=['prenom', 'nom', 'date'],keep=False)
    
    df = pd.merge(df1, df2, on=['prenom', 'nom', 'date'], how='outer', indicator='Source')
    
    df.to_csv(my_pandas_folder+'/MergeFirstLastDate.csv', encoding='utf8', index=False)