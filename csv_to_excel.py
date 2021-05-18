#convert csv in xlsx
import pandas as pd
from my_pandas_folder import *

def csv_to_excel(csv_file):
    df = pd.read_csv(csv_file)
    df.to_excel(my_pandas_folder+'/csv_convert.xlsx')