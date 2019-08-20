#Libraries
import pandas as pd 
import numpy as np
from datetime import datetime

#Cria um DataFrame a partir do arquivo CSV
df = pd.read_csv("file.csv", delimiter=";", low_memory=False)

#Novo Dataframe somente com orçamentos aprovados
approved = df.where(df.StatusTratamento=='APROVADO')
#Novo Dataframe somente com orçamentos NÃO aprovados
reproved = df.where(df.StatusTratamento=='NÃO APROVADO')

#Realizando o drop dos NaN's nas colunas de Idade
approvedAges = approved.Idade.dropna()
reprovedAges = reproved.Idade.dropna()
allAges = df.Idade.dropna()


print("Média de Idade - Aprovados=",approvedAges.median())
print("Média de Idade - Reprovados=",reprovedAges.median())
print("Média Geral=",allAges.median())
