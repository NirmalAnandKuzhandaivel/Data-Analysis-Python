# Question 2 Part 1

from pandas import Series, DataFrame
import pandas as pd
df1=pd.read_csv('~/Desktop/Python/Assignments/Data/employee_compensation.csv', sep=',', skiprows=(1,1))
dfq2=DataFrame(df1.groupby(["Organization Group", "Department"])['Total Compensation'].mean())
dfq2=dfq2.sort_values('Total Compensation', ascending=False).sort_index(level=0, sort_remaining=False)

dfq2.to_csv('question2Part1.csv', sep=',', encoding='utf-8')
dfq2.head()
