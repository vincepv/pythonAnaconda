import pandas as pd
import numpy as np
import math

def split_file(my_file):
    df = pd.read_csv(my_file)
    max_number_line_file = 24000
    number_chunk = math.ceil(len(df)/max_number_line_file)
    df = np.array_split(df, number_chunk)
    # df[0] = first array, last array df[n-1].
    i = number_chunk - 1
    while i > -1:
        df[i].to_csv("/Users/VPV/Desktop/pandas/Out%s.csv" % i, header=True, index=False, encoding="utf8")
        i = i - 1