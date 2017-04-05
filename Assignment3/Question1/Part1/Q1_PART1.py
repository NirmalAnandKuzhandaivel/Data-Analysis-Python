import calendar
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
vehicle_data=pd.read_csv("~/Desktop/Python/Assignments/Data/vehicle_collisions.csv",sep=",")
vehicle_data['Month'] = (pd.to_datetime(vehicle_data['DATE']).dt.month).apply(lambda x: calendar.month_abbr[x])
vehicle_data['Year'] =  (pd.to_datetime(vehicle_data['DATE']).dt.year)
vehicle_data=vehicle_data[vehicle_data.Year==2016]
df=DataFrame(vehicle_data,columns=['BOROUGH','Month'])
pdf_veh=df[df.BOROUGH=='MANHATTAN'].groupby(['Month']).count()
pdf_veh['NYC']=df[['BOROUGH','Month']].groupby(['Month']).count()
pdf_veh.columns=['MANHATTAN','NYC']
pdf_veh['PERCENTAGE']= pdf_veh['MANHATTAN']/pdf_veh['NYC']


pdf_veh.to_csv('question1Part1Analysis.csv', sep=',', encoding='utf-8')
pdf_veh.head()
