import pandas as pd
# csv utf8 
def merge_on_first_last_date(input1,input2):
    # input1 = electoral file
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    # clean file for merge, case sensitive
    df1['prenom'] = df1['prenom'].str.strip()
    df1['nom'] = df1['nom'].str.strip()

    df1['nom'] = df1['nom'].str.capitalize()
    df1['prenom'] = df1['prenom'].str.capitalize()

    df2['prenom'] = df2['prenom'].str.strip()
    df2['nom'] = df2['nom'].str.strip()

    df2['prenom'] = df2['prenom'].str.capitalize()
    df2['nom'] = df2['nom'].str.capitalize()
    
    # remove duplicate before merge, avoid to merge false data

    
    df = pd.merge(df1, df2, on=['prenom', 'nom', 'date'], how='outer', indicator='Source')

    df.to_csv('/Users/VPV/Desktop/Duplicate78.csv', encoding='utf8', index=False)