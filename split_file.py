import pandas as pd
import numpy as np
import math
from my_pandas_folder import *

def split_file(my_file_to_split):

    df = pd.read_csv(my_file_to_split, low_memory=False, encoding='latin1')
    max_number_line_file = 24500
    number_chunk = math.ceil(len(df)/max_number_line_file)
    df = np.array_split(df, number_chunk)
    # df[0] = first array, last array df[n-1].
    i = number_chunk - 1
    while i > -1:
        df[i].to_csv(my_pandas_folder+"/part_%s.csv" % i, header=True, index=False, encoding='latin1')
        i = i - 1