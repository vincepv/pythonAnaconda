import pandas as pd
from my_pandas_folder import *

def unique_address (my_file):
    df = pd.read_csv(my_file, low_memory=False)
    df = df.drop_duplicates(subset=['nom', 'adresse','cp'],keep='first')
    df.to_csv(my_pandas_folder+'/DraftUniqueAddress.csv', header=True, index=False, encoding="utf8")