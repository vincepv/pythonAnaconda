import numpy as np
import pandas as pd


def create_dummy_mobile(my_file):
    df = pd.read_csv( my_file ,low_memory = False)
    size_index=len(df)
    data = np.random.randint(10000001,99999999,size_index)
    df['mobile'] = data
    df.to_csv("/Users/VPV/Desktop/pandas/Out.csv",header=True,index=False,encoding="utf8",sep=',')
