#Question3
#!/usr/bin/python
import pandas as pd
import numpy as np


runs=pd.read_csv('~/Desktop/Python/Assignments/Data/cricket_matches.csv',sep=',')[['home','result','winner','innings1','innings1_runs','innings2','innings2_runs']]
runs['home_win']=np.where(runs['home']==runs['winner'],'YES','NO')

## Restrict data to home Winner
runs=runs[runs['home_win']=='YES']
runs['winner_score']=np.where(runs['winner']==runs['innings1'],runs['innings1_runs'],runs['innings2_runs'])
team_average=runs[['home','winner_score']]

## Average of Score

team_average=team_average.groupby('home').mean().sort_values(by =['winner_score'],ascending = False)
team_average.to_csv('question3Analysis.csv', sep=',', encoding='utf-8')
team_average.head()
