#Libraries
import pandas as pd 
import numpy as np
from datetime import datetime
from collections import Counter
import csv

#Cria um DataFrame a partir do arquivo CSV
df = pd.read_csv("file.csv", delimiter=";", low_memory=False)

 
def averageAge(df,statusCol, ageCol):

    #Novo Dataframe somente com orçamentos aprovados
    approved = df.where(df[statusCol]=='APROVADO')
    #Novo Dataframe somente com orçamentos NÃO aprovados
    reproved = df.where(df[statusCol]=='NÃO APROVADO')

    #Realizando o drop dos NaN's nas colunas de Idade
    approvedAges = approved[ageCol].dropna()
    reprovedAges = reproved[ageCol].dropna()
    generalAges = df[ageCol].dropna()

    #Exibe os resultados
    print("\nMédia de Idade - Aprovados=",approvedAges.median())
    print("Média de Idade - Reprovados=",reprovedAges.median())
    print("Média Geral=",generalAges.median())

#Realiza a contagem de H vs M de acordo com o Status do Orçamento
def genderCount(df, statusCol, genderCol):

    #Novo Dataframe somente com orçamentos aprovados
    approved = df.where(df[statusCol]=='APROVADO')
    #Novo Dataframe somente com orçamentos NÃO aprovados
    reproved = df.where(df[statusCol]=='NÃO APROVADO')

    #Realiza a contagem de Homens e Mulheres de acordo com o Status do Orçamento
    approvedGender = Counter(approved[genderCol])
    reprovedGender = Counter(reproved[genderCol])
    generalGender = Counter(df[genderCol])

    #Exibe os resultados
    print("\nGeneral")
    for item in generalGender.items():
        print(item)

    print("\nApproved")
    for item in approvedGender.items():
        print(item)
    
    print("\nReproved")
    for item in reprovedGender.items():
        print(item)
    
def customerCount(df,statusCol, codCliente):

    countApproved =0
    countReproved =0

    #Novo Dataframe somente com orçamentos aprovados
    approved = df.where(df[statusCol]=='APROVADO')
    #Novo Dataframe somente com orçamentos NÃO aprovados
    reproved = df.where(df[statusCol]=='NÃO APROVADO')

    uniqueApproved = approved.CodPac.unique()
    uniqueReproved = reproved.CodPac.unique()

    for a in uniqueApproved:
        countApproved+=1

    for r in uniqueReproved:
        countReproved+=1

    #Exibe os resultados
    print("\nClientes Unicos - Aprovados =",countApproved)
    print("\nClientes Unicos - Reprovados =",countReproved)

def treatmentCount(df, statusCol, codTratamento):

    countApproved =0
    countReproved =0

    #Novo Dataframe somente com orçamentos aprovados
    approved = df.where(df[statusCol]=='APROVADO')
    #Novo Dataframe somente com orçamentos NÃO aprovados
    reproved = df.where(df[statusCol]=='NÃO APROVADO')

    uniqueApproved = approved.CodTrat.unique()
    uniqueReproved = reproved.CodTrat.unique()

    for a in uniqueApproved:
        countApproved+=1

    for r in uniqueReproved:
        countReproved+=1

    print("\nTratamentos Aprovados =", countApproved)
    print("\nTratamentos Reprovados =", countReproved)


def money(df,statusCol,year):

    approved = df.where(df[statusCol]=='APROVADO')
    #Novo Dataframe somente com orçamentos NÃO aprovados
    reproved = df.where(df[statusCol]=='NÃO APROVADO')

    approvedTotalCopart = approved['TotalCoPart'].dropna()
    reprovedTotalCopart =  reproved['TotalCoPart'].dropna()

    print(str(year))
    #Aprovada
    print("Total CoParticipação - Aprovada=",approvedTotalCopart.sum())
    print("Média de CoParticipação - Aprovada=",approvedTotalCopart.mean())

    #Reprovada
    print("Total CoParticipação - Reprovada=",reprovedTotalCopart.sum())
    print("Média de CoParticipação - Reprovada=",reprovedTotalCopart.mean())

    print("\n\n\n")


def filterLeads(df, statusCol):

    approved = df.where(df[statusCol]=='APROVADO')
    #Novo Dataframe somente com orçamentos NÃO aprovados
    reproved = df.where(df[statusCol]=='NÃO APROVADO')

    #Lista onde será armazenados os Leads
    realLeads =[]

    c= open('leads.csv','a', newline='')
    writer = csv.writer(c)
    writer = csv.writer(c, delimiter=';')

    
    customers = approved['CodPac'].unique()
    potencialLeads = reproved['CodPac'].unique()

    for people in potencialLeads:
        if(people not in customers):
            realLeads.append(people)

    print("Clientes=",len(customers))
    print("Leads=",len(realLeads))

def filterDate (df,column,start_date, end_date):

    #Converte a coluna para o type datetime64[ns]
    df[column] = pd.to_datetime(df[column])

    #Cria uma máscara booleana com as datas de incío e termino
    mask = (df[column] > start_date ) & (df[column]<= end_date)

    #Realiza o filtro de acordo com a máscara
    df = df.loc[mask]

    #Retorna um novo dataframe
    return df

#Cria os Dataframes filtrados por ano
df2000 = filterDate(df,'DataIncio', '01/01/2000', '31/12/2000')
df2001 = filterDate(df,'DataIncio', '01/01/2001', '31/12/2001')
df2002 = filterDate(df,'DataIncio', '01/01/2002', '31/12/2002')
df2003 = filterDate(df,'DataIncio', '01/01/2003', '31/12/2003')
df2004 = filterDate(df,'DataIncio', '01/01/2004', '31/12/2004')
df2005 = filterDate(df,'DataIncio', '01/01/2005', '31/12/2005')
df2006 = filterDate(df,'DataIncio', '01/01/2006', '31/12/2006')
df2007 = filterDate(df,'DataIncio', '01/01/2007', '31/12/2007')
df2008 = filterDate(df,'DataIncio', '01/01/2008', '31/12/2008')
df2009 = filterDate(df,'DataIncio', '01/01/2009', '31/12/2009')
df2010 = filterDate(df,'DataIncio', '01/01/2010', '31/12/2010')
df2011 = filterDate(df,'DataIncio', '01/01/2011', '31/12/2011')
df2012 = filterDate(df,'DataIncio', '01/01/2012', '31/12/2012')
df2013 = filterDate(df,'DataIncio', '01/01/2013', '31/12/2013')
df2014 = filterDate(df,'DataIncio', '01/01/2014', '31/12/2014')
df2015 = filterDate(df,'DataIncio', '01/01/2015', '31/12/2015')
df2016 = filterDate(df,'DataIncio', '01/01/2016', '31/12/2016')
df2017 = filterDate(df,'DataIncio', '01/01/2017', '31/12/2017')
df2018 = filterDate(df,'DataIncio', '01/01/2018', '31/12/2018')
df2019 = filterDate(df,'DataIncio', '01/01/2019', '31/12/2019')



#lista com todos os dataframes
dataframes = [df2000, df2001, df2002,df2003,df2004, df2005, df2006, df2007, df2008, df2009, 
              df2010, df2011, df2012, df2013, df2014, df2015, df2016, df2017, df2018, df2019]
              
#Realiza o calculode idade média'StatusTratamento'
for dataframe in dataframes:

    averageAge(dataframe,'StatusTratamento','Idade')
    genderCount(dataframe,'StatusTratamento','Sexo')
    customerCount(dataframe,'StatusTratamento','CodPac')
    treatmentCount(dataframe, 'StatusTratamento','CodTrat')
    money(dataframe,'StatusTratamento',year)
