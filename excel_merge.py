# convert excel folder in one master utf8 csv file

import pandas as pd
import glob

def excel_merge(excel_folder):
    
    
    all_files = glob.glob(excel_folder + "/*.xlsx")
    li = []
    for filename in all_files:
        df = pd.read_excel(filename, index_col=None, header=0)
        li.append(df)
    df = pd.concat(li, axis=0, ignore_index=False, sort=True)
    df.to_csv('/Users/VPV/Desktop/excel_merge.csv', encoding= 'utf8', index=False, )