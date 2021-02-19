# clean csv utf8 file 
import pandas as pd

def clean_character(file_to_clean):
	
	df = pd.read_csv(file_to_clean)

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

	df.to_csv('/Users/VPV/Desktop/cleanCharacter.csv', encoding= 'utf8', index=False, )