import pandas as pd
from my_pandas_folder import *
 
def merge_on_electoral_phonebook (electoral_list,phone_book):


    """
    csv file in utf8
    electoral_list is the electoral list csv
    phone_book is the mobile or email csv to merge with electoral_list
    """

    df_electoral = pd.read_csv(electoral_list, low_memory=False)
    df_phonebook = pd.read_csv(phone_book, low_memory=False)

    # avoid case sensitive issue. Marc and MARC is different during merge process
  
    
    df_electoral['prenom'] = df_electoral['prenom'].str.strip()
    df_electoral['nom'] = df_electoral['nom'].str.strip()
    df_electoral['prenom'] = df_electoral['prenom'].str.capitalize()
    df_electoral['nom'] = df_electoral['nom'].str.capitalize()

    df_phonebook['prenom'] = df_phonebook['prenom'].str.strip()
    df_phonebook['nom'] = df_phonebook['nom'].str.strip()
    df_phonebook['prenom'] = df_phonebook['prenom'].str.capitalize()
    df_phonebook['nom']= df_phonebook['nom'].str.capitalize()

    
    # create duplicate file to tracks duplicate contact not in merge file

    df_dup_electoral = df_electoral[df_electoral.duplicated(['prenom', 'nom'], keep=False)]
    df_dup_phonebook = df_phonebook[df_phonebook.duplicated(['prenom', 'nom'], keep=False)]
    
    df_dup_electoral.to_csv(my_pandas_folder+'/DuplicateElectoral.csv', encoding='utf8', index=False)
    df_dup_phonebook.to_csv(my_pandas_folder+'/DuplicatePhoneBook.csv', encoding='utf8', index=False)
    
    # remove duplicate before merge, to avoid merge data to wrong contact

    df_electoral = df_electoral.drop_duplicates(subset=['prenom', 'nom'],keep=False)
    df_phonebook = df_phonebook.drop_duplicates(subset=['prenom', 'nom'],keep=False)
    
    df_merge = pd.merge(df_electoral, df_phonebook, on=['prenom', 'nom'], how='right', indicator='Source')
    
    # add duplicate phonebook to dataframe to avoid losing phonebook data.
    frames = [df_merge, df_dup_phonebook]
    df = pd.concat(frames, sort=True)
    
    # clean ".O" string
    df['cp'] = df['cp'].astype(str)
    df['cp'] = df['cp'].str.replace('\.0', '', regex=True)
    df['cp'] = df['cp'].str.replace('nan', '', regex=True)   
    
    df['sexe'] = df['sexe'].astype(str)
    df['sexe'] = df['sexe'].str.replace('\.0', '', regex=True)
    df['sexe'] = df['sexe'].str.replace('nan', '', regex=True)

    df['mobile'] = df['mobile'].astype(str)
    df['mobile'] = df['mobile'].str.replace('\.0', '', regex=True)
    df['mobile'] = df['mobile'].str.replace('nan', '', regex=True)

    df['categorie'] = df['categorie'].astype(str)
    df['categorie'] = df['categorie'].str.replace('\.0', '', regex=True)
    df['categorie'] = df['categorie'].str.replace('nan', '', regex=True)
    
    df.to_csv(my_pandas_folder+'/MergePhoneBook.csv', encoding='utf8', index=False)