import numpy as np
import pandas as pd
from my_pandas_folder import *

def create_dummy_mobile(my_file):
    df = pd.read_csv( my_file ,low_memory = False)
    size_index=len(df)
    data = np.random.randint(10000001,99999999,size_index)
    df['mobile'] = data
    df.to_csv(my_pandas_folder+"/create_dummy_mobile.csv",header=True,index=False,encoding="utf8",sep=',')
