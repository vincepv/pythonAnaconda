import pandas as pd
from my_pandas_folder import *
def autofill(my_file) :
    df = pd.read_csv(my_file, low_memory=False)
    df = df.ffill(axis=0)
    df.to_csv(my_pandas_folder+"/autofill.csv", header=True, index=False, encoding="utf8")