import pandas as pd
def extract_email_mobile(my_file):
    df = pd.read_csv(my_file)
    df.insert(loc=0, column='email_extract', value='')
    df.insert(loc=0, column='mobile_extract', value='')
    df['email_extract']=df['data'].str.extract(pat="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
    df['mobile_extract']=df['data'].str.extract(pat="(\d{10})")
    df.to_csv("/Users/VPV/Desktop/Out.csv",header=True,index=False,encoding="utf8")
