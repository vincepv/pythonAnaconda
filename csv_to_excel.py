#convert csv in xlsx
import pandas as pd

def csv_to_excel(csv_file):
	df = pd.read_csv(csv_file)
	df.to_excel('/Users/VPV/Desktop/csv_convert.xlsx')