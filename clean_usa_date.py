import pandas as pd
from my_pandas_folder import *

def clean_usa_date(my_file):
    df = pd.read_csv(my_file, low_memory=False)

    df['date'] = df['date'].astype(str)

    # clean month with 2 digits : m to mm

    df['date'] = df['date'].str.replace('^1/', '01/', regex=True)
    df['date'] = df['date'].str.replace('^2/', '02/', regex=True)
    df['date'] = df['date'].str.replace('^3/', '03/', regex=True)
    df['date'] = df['date'].str.replace('^4/', '04/', regex=True)
    df['date'] = df['date'].str.replace('^5/', '05/', regex=True)
    df['date'] = df['date'].str.replace('^6/', '06/', regex=True)
    df['date'] = df['date'].str.replace('^7/', '07/', regex=True)
    df['date'] = df['date'].str.replace('^8/', '08/', regex=True)
    df['date'] = df['date'].str.replace('^9/', '09/', regex=True)

    # clean day with 2 digits : d to dd

    df['date']=df['date'].str.replace('/1/', '/01/', regex=True)
    df['date']=df['date'].str.replace('/2/', '/02/', regex=True)
    df['date']=df['date'].str.replace('/3/', '/03/', regex=True)
    df['date']=df['date'].str.replace('/4/', '/04/', regex=True)
    df['date']=df['date'].str.replace('/5/', '/05/', regex=True)
    df['date']=df['date'].str.replace('/6/', '/06/', regex=True)
    df['date']=df['date'].str.replace('/7/', '/07/', regex=True)
    df['date']=df['date'].str.replace('/8/', '/08/', regex=True)
    df['date']=df['date'].str.replace('/9/', '/09/', regex=True)



    # creation d'une colonnes qui va recevoir l'extraction de la date 
    df.insert(loc=0, column='jour', value='N/A')
    df.insert(loc=0, column='mois', value='N/A')
    df.insert(loc=0, column='annee', value='N/A')
    df['mois'] = df['date'].str[:2]
    df['jour'] = df['date'].str[3:-5]
    df['annee'] = df['date'].str[6:]
    df['date'] = df['annee']+ "-" + df['mois']+ "-" + df['jour']
    #transforme les colonnes vides en N/A
    df['date'] = df['date'].replace(['--na','--N/'],'N/A' , regex=True)
    df = df.drop(['jour', 'mois', 'annee'], axis=1)

    df.to_csv(my_pandas_folder"/clean_usa_date.csv",header=True,index=False,encoding="utf8",sep=',')
