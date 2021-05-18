#merge all sheets of one excel in one csv
import pandas as pd
from my_pandas_folder import *
def merge_excel_sheet(excel_file):
    df = pd.concat(pd.read_excel(excel_file, sheet_name=None), ignore_index=True)
    df.to_csv(my_pandas_folder+'/merge_excel_sheet.csv')