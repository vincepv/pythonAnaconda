import pandas as pd
from my_pandas_folder import *
def generate_firstname_lastname(my_file) :
    
    """Generate FirstName and lastName with email
    
    important : Need 'email' column ! 
    
    """
    
    df = pd.read_csv(my_file, low_memory=False)
    # create column
    df['create_prenom'] = df.loc[:, 'email']
    df['create_nom'] = df.loc[:, 'email']
    # clean prenom
    remove_character = {
        '(?=@).*': '',
        '\.': ' ',
        '\d': ' ',
        '-': '', 
        '_': '',
        '    ':' ',
        '   ':' ',
        '  ': ' ',
        '^ ': '',
        ' $': ''
    }
    df['create_prenom'] = df['create_prenom'].replace(remove_character, regex=True)
    # clean nom
    df['create_nom'] = df['create_nom'].replace(remove_character, regex=True)
    df.to_csv(my_pandas_folder+"/generateName.csv", header=True, index=False, encoding="utf8")
    