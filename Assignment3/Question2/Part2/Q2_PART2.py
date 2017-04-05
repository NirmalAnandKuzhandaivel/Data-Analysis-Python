from pandas import Series, DataFrame
import pandas as pd
import numpy as np
data=pd.read_csv('~/Desktop/Python/Assignments/Data/employee_compensation.csv',sep=',')

# Filter the data based on year type Calendar

calendar_data=DataFrame(data,columns=['Year Type','Employee Identifier','Salaries','Overtime','Other Salaries','Total Salary','Total Benefits','Total Compensation'])
calendar_data=calendar_data[calendar_data['Year Type']=='Calendar']
calendar_data=calendar_data.groupby(by=['Employee Identifier']).mean()

#Filter Who worked Overtime

calendar_data['Five Percent Salary']=calendar_data['Salaries']*0.05
calendar_data['Is OverTime More']=np.where(calendar_data['Overtime']>calendar_data['Five Percent Salary'],'YES','NO')
calendar_data=calendar_data[calendar_data['Is OverTime More']=='YES']

#Take the Employee Identifiers of filtered data

employee_data = DataFrame(calendar_data.index.get_level_values('Employee Identifier'))

#Filter Job Family data

job_family_data = employee_data.merge(data, on = 'Employee Identifier')['Job Family'].unique()
jf = data[data['Job Family'].isin(job_family_data)]
jf = jf.groupby('Job Family')['Total Benefits', 'Total Compensation'].mean()

#Calculate Total benefit and sort

jf['Percent_Total_Benefit'] = jf['Total Benefits'] * 100 / jf['Total Compensation']
jf=jf.sort_values(by='Percent_Total_Benefit', ascending=False).head(n=5)
jf.to_csv('question2Part2Analysis.csv', sep=',', encoding='utf-8')
jf.head()
