import pandas as pd

import numpy as np

#confirmed cases spreadsheet

COVID19_global_cases = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

COVID19_global_cases_new = COVID19_global_cases.drop(['Province/State','Lat','Long'], axis=1)

print(COVID19_global_cases_new)

#COVID19_global_cases_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new.csv',index=False)

COVID19_global_cases_sum = COVID19_global_cases_new.groupby(['Country/Region']).sum()

COVID19_global_cases_transpose = COVID19_global_cases_sum.T.reset_index()

COVID19_global_cases_melt = COVID19_global_cases_transpose.melt(id_vars= 'index', var_name='Country', value_name='cases')

COVID19_global_cases_melt['ratio'] = 1
COVID19_global_cases_melt['new_cases'] = 0

for index, row in COVID19_global_cases_melt.iterrows():
    if((COVID19_global_cases_melt.loc[index]['cases'] == 0) or (COVID19_global_cases_melt.loc[index-1]['cases'] == 0)):
        COVID19_global_cases_melt.loc[index,'ratio'] = 1
    else:
        COVID19_global_cases_melt.loc[index,'ratio'] = COVID19_global_cases_melt.loc[index]['cases']/COVID19_global_cases_melt.loc[index-1]['cases']
        COVID19_global_cases_melt.loc[index,'new_cases'] = COVID19_global_cases_melt.loc[index]['cases'] - COVID19_global_cases_melt.loc[index-1]['cases']
        Cases_1 = COVID19_global_cases_melt.loc[index,'ratio']
        Cases_2 = COVID19_global_cases_melt.loc[(index-1),'ratio']
        Cases_3 = COVID19_global_cases_melt.loc[(index-2),'ratio']
        COVID19_global_cases_melt.loc[index,'ratio'] = (Cases_1 + Cases_2 + Cases_3) / 3

COVID19_global_cases_melt = COVID19_global_cases_melt.rename(columns={"index" : "date"})

#COVID19_global_cases_melt.columns=["date", "country", "cases"]

#COVID19_global_cases_melt = COVID19_global_cases_melt.columns["date", "country", "cases"]

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.droplevel(level=0)

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.drop(['Guam','Northern Mariana Islands','American Samoa','Diamond Princess','Grand Princess'], axis=1)

#print(COVID19_global_cases_transpose.head())

#COVID19_global_cases_new_transpose.head().to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new_head.csv')

#COVID19_global_cases_new_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new_transpose.csv')

COVID19_global_cases_melt.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_melt.csv', index = False)

#move on to the deaths spreadsheet

COVID19_global_deaths = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_deaths_global.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

COVID19_global_deaths_new = COVID19_global_deaths.drop(['Province/State','Lat','Long'], axis=1)

print(COVID19_global_deaths_new)

#COVID19_global_cases_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new.csv',index=False)

COVID19_global_deaths_sum = COVID19_global_deaths_new.groupby(['Country/Region']).sum()

COVID19_global_deaths_transpose = COVID19_global_deaths_sum.T.reset_index()

COVID19_global_deaths_melt = COVID19_global_deaths_transpose.melt(id_vars= 'index', var_name='Country', value_name='deaths')

COVID19_global_deaths_melt['ratio'] = 1

for index, row in COVID19_global_deaths_melt.iterrows():
    if((COVID19_global_deaths_melt.loc[index]['deaths'] == 0) or (COVID19_global_deaths_melt.loc[index-1]['deaths'] == 0)):
        COVID19_global_deaths_melt.loc[index,'ratio'] = 1
    else:
        COVID19_global_deaths_melt.loc[index,'ratio'] = COVID19_global_deaths_melt.loc[index]['deaths']/COVID19_global_deaths_melt.loc[index-1]['deaths']
        Cases_1 = COVID19_global_deaths_melt.loc[index,'ratio']
        Cases_2 = COVID19_global_deaths_melt.loc[(index-1),'ratio']
        Cases_3 = COVID19_global_deaths_melt.loc[(index-2),'ratio']
        COVID19_global_deaths_melt.loc[index,'ratio'] = (Cases_1 + Cases_2 + Cases_3) / 3

COVID19_global_deaths_melt = COVID19_global_deaths_melt.rename(columns={"index" : "date"})

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.droplevel(level=0)

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.drop(['Guam','Northern Mariana Islands','American Samoa','Diamond Princess','Grand Princess'], axis=1)

#print(COVID19_global_cases_transpose.head())

#COVID19_global_cases_new_transpose.head().to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new_head.csv')

#COVID19_global_cases_new_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new_transpose.csv')

COVID19_global_deaths_melt.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_deaths_melt.csv', index = False)