import pandas as pd
def autofill(my_file) :
    df = pd.read_csv(my_file,low_memory = False)
    df = df.ffill(axis = 0)
    df.to_csv("/Users/VPV/Desktop/Out.csv",header=True,index=False,encoding="utf8")