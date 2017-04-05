# Question 2 Part 1

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
data=pd.read_csv("/Users/nirmal/Desktop/Python/Assignments/Data/vehicle_collisions.csv",sep=",")
pdf=DataFrame(data, columns=['BOROUGH', 'VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'])

pdf['VEHICLE 1 TYPE'] = pdf['VEHICLE 1 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
pdf['VEHICLE 2 TYPE'] = pdf['VEHICLE 2 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
pdf['VEHICLE 3 TYPE'] = pdf['VEHICLE 3 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
pdf['VEHICLE 4 TYPE'] = pdf['VEHICLE 4 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
pdf['VEHICLE 5 TYPE'] = pdf['VEHICLE 5 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)
pdf['COMBINE']=pdf['VEHICLE 1 TYPE']+pdf['VEHICLE 2 TYPE']+pdf['VEHICLE 3 TYPE']+pdf['VEHICLE 4 TYPE']+\
    pdf['VEHICLE 5 TYPE']
pdf['COMBINE']=pdf['COMBINE'].apply(lambda x: 4 if x>3 else x)

pdf['ONE VEHICLE INVOLVED']= np.where(pdf['COMBINE']== 1, 1,0)
pdf['TWO VEHICLE INVOLVED']= np.where(pdf['COMBINE']== 2, 1,0)
pdf['THREE VEHICLE INVOLVED']= np.where(pdf['COMBINE']== 3, 1,0)
pdf['MORE VEHICLES INVOLVED']= np.where(pdf['COMBINE']== 4, 1,0)
pdf=pdf.groupby('BOROUGH').sum()

outputpdf=DataFrame(pdf,columns=['ONE VEHICLE INVOLVED','TWO VEHICLE INVOLVED','THREE VEHICLE INVOLVED','MORE VEHICLES INVOLVED'])


outputpdf.to_csv('question1Part2Analysis.csv', sep=',', encoding='utf-8')
outputpdf.head()
