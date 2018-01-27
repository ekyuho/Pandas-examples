# coding: utf-8
import requests
import pandas as pd
import io

url = 'https://docs.google.com/spreadsheets/d/KEY/gviz/tq?tqx=out:csv&sheet={시트이름}'
s=requests.get(url).content
names = ['time', 'personal', 'major', 'prog','q','history']
df=pd.read_csv(io.StringIO(s.decode('utf-8')))
df.columns = ['time','personal','grad','prog','q','history','p7','p8']
df[['name','begin','end','mobile','email']] = df['personal'].str.split('/', expand=True)
df[['class','major','major2','major3']] = df['grad'].str.split('/', expand=True)
df2 = df[['major','major2','name','mobile','email']][df['prog'].str.contains('1. 블라블라')]

import os
os.chdir('D:/work')

file_name='file.csv'
df2.to_csv(file_name, sep=',', encoding='utf-8-sig')
