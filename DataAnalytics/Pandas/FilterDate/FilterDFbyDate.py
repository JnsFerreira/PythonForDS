import pandas as pd 
from datetime import datetime
from collections import Counter

#Cria um DataFrame a partir do arquivo CSV
df = pd.read_csv("file.csv", delimiter=";", low_memory=False)

def filterDate (df,column,start_date, end_date):

    #Converte a coluna para o type datetime64[ns]
    df[column] = pd.to_datetime(df[column])

    #Cria uma máscara booleana com as datas de incío e termino
    mask = (df[column] > start_date ) & (df[column]<= end_date)

    #Realiza o filtro de acordo com a máscara
    df = df.loc[mask]

    #Retorna um novo dataframe
    return df

def filterCustomers(df):

    mask = (Counter(df['CodPac']>2))

    df = df.loc[mask]

    print(df)

df2017_2019= filterDate(df,'DataIncio','01/01/2017','01/07/2019')
df2014_2019= filterDate(df,'DataIncio','01/01/2014','01/07/2019')

contador = Counter (df['CodPac'])

for item in contador.items():
    print(item)
