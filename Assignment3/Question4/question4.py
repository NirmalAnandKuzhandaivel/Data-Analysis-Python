import pandas as pd
import numpy as np
import re
df=pd.read_csv('/Users/nirmal/Desktop/Python/Assignments/Data/movies_awards.csv',sep=',')[['Title','Awards']]
df.head()


df['Awards_won'] = df['Awards'].str.extract('(\d+) w', expand=True).fillna(0)
df['Awards_Nominated']  = df['Awards'].str.extract('(\d+) n', expand=True).fillna(0)
df['Bafta_Awards_Nominated']  = df['Awards'].str.extract('Nominated for (\d+) BAFT', expand=True).fillna(0)
df['Oscar_Awards_Nominated']  = df['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True).fillna(0)
df['Prime_Awards_Nominated'] = df['Awards'].str.extract('Nominated for (\d+) Prime', expand=True).fillna(0)
df['Golden_Globe_Awards_Nominated'] = df['Awards'].str.extract('Nominated for (\d+) Golden', expand=True).fillna(0)
df['Bafta_Awards_Won']  = df['Awards'].str.extract('Won (\d+) BAFTA', expand=True).fillna(0)
df['Oscar_Awards_Won']  = df['Awards'].str.extract('Won (\d+) Oscar[s]?', expand=True).fillna(0)
df['Prime_Awards_Won'] = df['Awards'].str.extract('Won (\d+) Prime', expand=True).fillna(0)
df['Golden_Globe_Awards_Won'] = df['Awards'].str.extract('Won (\d+) Golden', expand=True).fillna(0)


df[['Awards_won','Awards_Nominated']]=df[['Awards_won','Awards_Nominated']].apply(pd.to_numeric,errors='ignore')
df[['Bafta_Awards_Nominated']]=df[['Bafta_Awards_Nominated']].apply(pd.to_numeric,errors='ignore')
df[['Oscar_Awards_Nominated']]=df[['Oscar_Awards_Nominated']].apply(pd.to_numeric,errors='ignore')
df[['Prime_Awards_Nominated']]=df[['Prime_Awards_Nominated']].apply(pd.to_numeric,errors='ignore')
df[['Golden_Globe_Awards_Nominated']]=df[['Golden_Globe_Awards_Nominated']].apply(pd.to_numeric,errors='ignore')
df[['Bafta_Awards_Won']]=df[['Bafta_Awards_Won']].apply(pd.to_numeric,errors='ignore')
df[['Oscar_Awards_Won']]=df[['Oscar_Awards_Won']].apply(pd.to_numeric,errors='ignore')
df[['Prime_Awards_Won']]=df[['Prime_Awards_Won']].apply(pd.to_numeric,errors='ignore')
df[['Golden_Globe_Awards_Won']]=df[['Golden_Globe_Awards_Won']].apply(pd.to_numeric,errors='ignore')


df['Awards_won']=df['Awards_won'] + df['Bafta_Awards_Won']+df['Oscar_Awards_Won']+\
    df['Prime_Awards_Won']+df['Golden_Globe_Awards_Won']


df['Awards_Nominated']=df['Awards_Nominated']+df['Bafta_Awards_Nominated']+\
    df['Oscar_Awards_Nominated']+df['Prime_Awards_Nominated']+df['Golden_Globe_Awards_Nominated']

df.to_csv('AwardsFinal.csv', sep=',', encoding='utf-8')
