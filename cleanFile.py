# Script DigitaleBox for clean csv file
# csv delimitor , encoding utf-8
# column must be renamed
#
# __'prenom' 
# __'nom' 
# __'sexe' 
# --'adresse'
# __'cp' 
# __'ville'
# __'date' (date de naissance au format jj/mm/aaaa)
# __'note'
# __'mot clef'
# __'email'
# __'mobile' 
# Don't forget to mentioned my_file (old) and my_clean_file (new)

import pandas as pd
import numpy as np

my_file =''
motclef = ''
    
    
df = pd.read_csv( my_file ,low_memory = False)



# clean header 

df.columns = df.columns.str.lower()
df.columns = df.columns.str.strip()

# create column if not in csv

if 'categorie' not in df:
	df.insert(loc=0, column='categorie', value='2')    
if 'note' not in df:
	df.insert(loc=0, column='note', value='')
if 'mot clef' not in df:
	df.insert(loc=0, column='mot clef', value=motclef)
else:
    df['mot clef']=df['mot clef']+','+motclef
if 'sexe' not in df:
	df.insert(loc=0, column='sexe', value='0')
else :
    df['sexe']=df['sexe'].fillna('N/A')
    
if 'prenom' not in df:
    df.insert(loc=0, column='prenom', value='') 

if 'nom' not in df:
    df.insert(loc=0, column='nom', value='') 

if 'pays' not in df:
	df.insert(loc=0, column='pays', value='FR')
else:
    df['pays']=df['pays'].astype(str)
    df['pays']=df['pays'].replace(['FRANCE','france','France'],'FR')
    df['pays']=df['pays'].replace(['nan'],'N/A')

if 'ville' not in df:
	df.insert(loc=0, column='ville', value='N/A')
else : 
    df['ville']=df['ville'].fillna('N/A')

if 'cp' not in df:
	df.insert(loc=0, column='cp', value='N/A')
else : 
    df['cp']=df['cp'].fillna('N/A')

if 'adresse' not in df:
	df.insert(loc=0, column='adresse', value='N/A')
else : 
    df['adresse']=df['adresse'].fillna('N/A')
    
if 'date' not in df:
	df.insert(loc=0, column='date', value='N/A')
if 'mobile' not in df:
    df.insert(loc=0, column='mobile', value='N/A')
else:
    df['mobile']=df['mobile'].fillna('')

if 'email' not in df:
    df.insert(loc=0, column='email', value='N/A')
else:
    df['email']=df['email'].fillna('')


# fill empty firstname and lastname with organisation, then clean it

if 'organisme' in df:
    df['nom'] = df['nom'].fillna(df['organisme'])
    df['prenom'] = df['prenom'].fillna(df['organisme'])

dic_organisme = { '\d':'', '\.':'' , '&':'et' }    
df['nom'] = df['nom'].replace(dic_organisme,regex=True)
df['nom'] = df['nom'].str.strip()

df['prenom'] = df['prenom'].replace(dic_organisme,regex=True)
df['prenom'] = df['prenom'].str.strip()

# Email 

df['email']=df['email'].astype(str)
dic_email = {',':'.' , ';':'.' , 'ç':'c' , 'é':'e', 'è':'e' }
df['email']=df['email'].replace(dic_email, regex=True)
df['email']=df['email'].str.strip()
    
# Consider date as a string, change date dd-mm-yyyy > yyyy-mm-dd

df['date']=df['date'].astype(str)
# creation d'une colonnes qui va recevoir l'extraction de la date 
df.insert(loc=0, column='jour',value='N/A')
df.insert(loc=0, column='mois',value='N/A')
df.insert(loc=0, column='annee',value='N/A')
df['jour'] = df['date'].str[:2]
df['mois'] = df['date'].str[3:-5]
df['annee'] = df['date'].str[6:]
df['date'] = df['annee']+ "-" + df['mois']+ "-" + df['jour']
#transforme les colonnes vides en N/A
df['date'] = df['date'].replace(['--na','--N/'],'N/A' , regex=True)
df=df.drop(['jour', 'mois', 'annee'], axis=1)

# clean gender

df['sexe']=df['sexe'].astype(str)
df['sexe']=df['sexe'].str.replace('\.0$', '', regex=True)
df['sexe']=df['sexe'].str.strip()
df['sexe']=df['sexe'].replace(['monsieur','Monsieur','MONSIEUR','Mr', 'MR','M.','M','mr','m'],'2')
df['sexe']=df['sexe'].replace(['madame','Madame','MADAME','Ms','MS','Mme','MME','Mlle','MLLE','Mme','F','mme'],'1')    


# clean for geocoding

df['adresse']=df['adresse'].astype(str)
df['adresse']=df['adresse'].str.replace(',', '', regex=True)
df['adresse']=df['adresse'].str.strip()

# zip code


df['cp']=df['cp'].astype(str)
df['cp']=df['cp'].str.replace('\.0$', '', regex=True)

# clean mobile

df['mobile']=df['mobile'].astype(str)
dic_mobile_character = {'\.0$':'' , ' ': '' , '\.': '' , '\-': '' , '\_': '' , '\(': '' , '\)': '', '\,':'' }
dic_mobile_number = { '^06':'+336', '^07':'+337', '^6':'+336', '^7':'+337' }
df['mobile']=df['mobile'].replace(dic_mobile_character, regex=True)
df['mobile']=df['mobile'].replace(dic_mobile_number, regex=True)

    
#remove duplicate email and mobile, keep first, keep row for duplicates

df = df.drop_duplicates()
df.loc[df['email'].duplicated(), ['email']] = ''
df.loc[df['mobile'].duplicated(), ['mobile']] = ''    


# extract mobile and phone


df.insert(loc=0, column='cleanMobile', value='N/A')
df.insert(loc=0, column='cleanFixe', value='N/A')

df['cleanMobile'] = df['mobile'].str.findall('^\+33.+')
df['cleanFixe'] = df['mobile'].str.findall('^0.+|^1.+|^2.+|^3.+|^4.+|^5.+|^8.+|^9.+')

dic_clean_mobile = {'\[':'' ,'\]':'','\'':''}
df['cleanMobile'] = df['cleanMobile'].astype(str)
df['cleanMobile'] = df['cleanMobile'].replace(dic_clean_mobile , regex=True)

df['cleanFixe'] = df['cleanFixe'].astype(str)
df['cleanFixe'] = df['cleanFixe'].replace(dic_clean_mobile , regex=True)

df.to_csv('/Users/VPV/Desktop/pandas/DraftCleanFile.csv',header=True,index=False,encoding="utf8")