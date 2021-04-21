import pandas as pd
import numpy as np


def clean_electoral(mon_fichier):

    df = pd.read_csv(mon_fichier, low_memory=False)

    # check columns in csv
    if 'categorie' not in df:
        df.insert(loc=0, column='categorie', value='3')
    if 'note' not in df:
        df.insert(loc=0, column='note', value='')
    if 'mot clef' not in df:
        df.insert(loc=0, column='mot clef', value='')
    if 'sexe' not in df:
        df.insert(loc=0, column='sexe', value='0')
    if 'prenom' not in df:
        df.insert(loc=0, column='prenom', value='prenom a renseigner')
    else:
        df['prenom'] = df['prenom'].fillna('A')
    if 'pays' not in df:
        df.insert(loc=0, column='pays', value='FR')
    else:
        df['pays'] = df['pays'].astype(str)
        df['pays'] = df['pays'].replace(['FRANCE', 'france', 'France'], 'FR')
        df['pays'] = df['pays'].replace(['nan'], 'N/A')
    if 'ville' not in df:
        df.insert(loc=0, column='ville', value='N/A')
    if 'cp' not in df:
        df.insert(loc=0, column='cp', value='N/A')
    if 'adresse' not in df:
        df.insert(loc=0, column='adresse', value='N/A')
    if 'rue' not in df:
        df.insert(loc=0, column='rue', value='N/A')
    if 'numero' not in df:
        df.insert(loc=0, column='numero', value='N/A')
    if 'date' not in df:
        df.insert(loc=0, column='date', value='N/A')
    if 'mobile' not in df:
        df.insert(loc=0, column='mobile', value='N/A')
    else:
        df['mobile'] = df['mobile'].fillna('N/A')

    if 'email' not in df:
        df.insert(loc=0, column='email', value='N/A')
    else:
        df['email'] = df['email'].fillna('N/A')

    # si le nom usage est vide, on le remplit avec le nom de naissance, evite un nom usage vide
    df['nomUsage'] = df['nomUsage'].fillna(df['nomNaissance'])

    # date of birth in yyyy-mm-dd format
    df['date'] = df['date'].astype(str)
    # clean invalide date 00/00/1976 = 01/01/1976
    df["date"] = df["date"].str.replace('^00', '01', regex=True)
    df["date"] = df["date"].str.replace('/00/', '/01/', regex=True)
    df.insert(loc=0, column='jour', value='N/A')
    df.insert(loc=0, column='mois', value='N/A')
    df.insert(loc=0, column='annee', value='N/A')
    df['jour'] = df['date'].str[:2]
    df['mois'] = df['date'].str[3:-5]
    df['annee'] = df['date'].str[6:]
    df['date'] = df['annee'] + "-" + df['mois'] + "-" + df['jour']
    # transforme les colonnes vides en N/A
    df['date'] = df['date'].replace(['--na', '--N/'], 'N/A', regex=True)
    df = df.drop(['jour', 'mois', 'annee'], axis=1)

    # clean gender

    df['sexe'] = df['sexe'].fillna('0')
    df['sexe'] = df['sexe'].astype(str)
    # transforme 1.0 et 2.0 en 1 et 2
    df['sexe'] = df['sexe'].str.replace('\.0$', '', regex=True)
    df['sexe'] = df['sexe'].str.replace(' ', '', regex=True)
    df['sexe'] = df['sexe'].replace(['monsieur', 'Monsieur', 'MONSIEUR', 'Mr', 'MR', 'M.', 'M', 'mr', 'm'], '2')
    df['sexe'] = df['sexe'].replace(['madame', 'Madame', 'MADAME', 'Ms', 'MS', 'Mme', 'MME', 'Mlle', 'MLLE', 'Mme', 'F', 'mme'], '1')

    # clean address

    df['numero'] = df['numero'].astype(str)
    df['rue'] = df['rue'].astype(str)
    df['adresse'] = df['numero']+' '+df['rue']
    df['adresse'] = df['adresse'].str.replace(',', '', regex=True)
    df['adresse'] = df['adresse'].str.replace('^ ', '', regex=True)
    df['adresse'] = df['adresse'].str.replace(' $', '', regex=True)

    # renomme les cellules vides issues provenant de numeroe et rue
    df['adresse'] = df['adresse'].str.replace('nan', '', regex=True)
    df['adresse'] = df['adresse'].str.replace('N/A N/A', 'N/A', regex=True)

    # clean zip
    df['cp'] = df['cp'].fillna('N/A')
    df['cp'] = df['cp'].astype(str)
    df['cp'] = df['cp'].str.replace('\.0$', '', regex=True)

    # keep begining of first name
    df['prenom'] = df['prenom'].str.split(n=1, expand=True)
    df['prenom'] = df['prenom'].str.capitalize()

    # keyword
    if 'numero bv' in df:
        df['numero bv'] = df['numero bv'].astype(str)
        #creation des mot clefs : BV xxx + LE
        df['mot clef'] = df['mot clef']+','+'BV '+df['numero bv']+','+'LE2020'

    else:
        df['mot clef'] = df['mot clef'].str.replace('X', 'V1TM2020', regex=True)
        df['mot clef'] = df['mot clef'].str.replace('x', 'V1TM2020', regex=True)

    df['mot clef'] = df['mot clef'].astype(str)
    df['mot clef'] = df['mot clef'].str.replace('\.0$', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace('nan', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace('^,', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace(';', ',', regex=True)

    # clean mobile
    df['mobile'] = df['mobile'].astype(str)
    dic_mobile_character = {'\.0$': '', ' ': '', '\.': '', '\-': '', '\_': '', '\(': '', '\)': '', '\,': ''}
    dic_mobile_number = {'^06': '+336', '^07': '+337', '^6': '+336', '^7': '+337'}
    df['mobile'] = df['mobile'].replace(dic_mobile_character, regex=True)
    df['mobile'] = df['mobile'].replace(dic_mobile_number, regex=True)
    
    df = df.drop_duplicates(subset=['prenom', 'nomUsage', 'nomNaissance', 'date'],keep='first')
    
    df.to_csv("/Users/VPV/Desktop/pandas/clean_electoral.csv", header=True, index=False, encoding="utf8")