#clean broken character with french accent 
import pandas as pd

def accent(csv_file):
	df = pd.read_csv(csv_file)
	df=df.replace('Ã©', 'é', regex=True)
	df=df.replace('Ã¨', 'è', regex=True)
	df=df.replace('Ã«', 'ë', regex=True)
	df=df.replace('Ã§', 'ç', regex=True)
	df=df.replace('Ã®', 'ï', regex=True)
	df=df.replace('Ã‰', 'E', regex=True)
	df=df.replace('Ã”', 'O', regex=True)
	df=df.replace('Ã¢', 'â', regex=True)
	df=df.replace('Ã¯', 'ï', regex=True)
	df=df.replace('Ã´', 'ô', regex=True)
	df=df.replace('Ãª', 'ê', regex=True)
	df=df.replace('Ãˆ', 'E', regex=True)
	df.to_csv('/Users/VPV/Desktop/pandas/accent.csv', encoding='utf8', index=False)
