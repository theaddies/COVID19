import pandas as pd
#confirmed cases spreadsheet

COVID19_global_cases = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

COVID19_global_cases_new = COVID19_global_cases.drop(['Province/State','Lat','Long'], axis=1)

print(COVID19_global_cases_new)

COVID19_global_cases_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new.csv',index=False)

COVID19_global_cases_new_sum = COVID19_global_cases_new.groupby(['Country/Region'],as_index=False).sum()

COVID19_global_cases_new_sum.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new_sum.csv')


COVID19_global_cases_new_transpose = COVID19_global_cases_new_sum.T

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.droplevel(level=0)

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.drop(['Guam','Northern Mariana Islands','American Samoa','Diamond Princess','Grand Princess'], axis=1)

print(COVID19_global_cases_new_transpose.head())

COVID19_global_cases_new_transpose.head().to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new_head.csv')

COVID19_global_cases_new_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_new_transpose.csv')

COVID19_global_cases_new_transpose.melt(var_name='state', value_name='value').to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_cases_melt.csv')

#move on to the deaths spreadsheet

COVID19_global_deaths = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_deaths_global.csv')

COVID19_global_deaths_new = COVID19_global_deaths.drop(['Province/State','Lat','Long'], axis=1)

print(COVID19_global_deaths_new)

COVID19_global_deaths_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_deaths_new.csv',index=False)

COVID19_global_deaths_new_sum = COVID19_global_deaths_new.groupby(['Country/Region']).sum()

COVID19_global_deaths_new_sum.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_deaths_new_sum.csv')

COVID19_global_deaths_new_transpose = COVID19_global_deaths_new_sum.T

#COVID19_global_deaths_new_transpose = COVID19_global_deaths_new_transpose.drop(['Guam','Northern Mariana Islands','American Samoa','Diamond Princess','Grand Princess'], axis=1)

print(COVID19_global_deaths_new_transpose)

COVID19_global_deaths_new_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_deaths_new_transpose.csv')

COVID19_global_deaths_new_transpose.melt(var_name='country', value_name='value').to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_global_deaths_melt.csv')
print(COVID19_global_deaths_new_transpose.melt(var_name='country', value_name='value'))