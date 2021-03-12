# merge a folder with utf8 csv in one master csv file

import pandas as pd
import glob

def csv_merge(folder_csv): 
    """
    indique le dossier csv à traiter
    """
	all_files = glob.glob(folder_csv + "/*.csv")

	li = []

	for filename in all_files:
	    df = pd.read_csv(filename, index_col=None, header=0)
	    li.append(df)

	df = pd.concat(li, axis=0, ignore_index=False, sort=True)

	df.to_csv('/Users/VPV/Desktop/DraftCsvMerge.csv', encoding= 'utf8', index=False)