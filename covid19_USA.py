import pandas as pd

#confirmed cases spreadsheet
#url1 = "https://github.com/CSSEGISandData/COVID-19/blame/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"

pd.set_option('display.expand_frame_repr', True)

#COVID19_US_cases = pd.read_csv(url1,sep=',',skiprows=[33,242,243,244],engine='python', error_bad_lines=False)

#COVID19_US_cases.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_cases_bk.csv')
                                                             
COVID19_US_cases = pd.read_csv(r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

COVID19_US_cases_new = COVID19_US_cases.drop(['UID','iso2','iso3','code3','FIPS','Country_Region','Combined_Key','Lat','Long_'], axis=1)

print(COVID19_US_cases_new)

#COVID19_US_cases_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_cases_new.csv',index=False)

#COVID19_US_cases_new = COVID19_US_cases_new.rename(columns = {'Admin2' : 'County'})

COVID19_US_cases_sum = COVID19_US_cases_new.groupby(['Province_State']).sum()

#COVID19_US_cases_new_sum.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_cases_new_sum.csv')

COVID19_US_cases_transpose = COVID19_US_cases_sum.T.reset_index()

print(COVID19_US_cases_transpose)

#melt_df = org_df.reset_index().melt(id_vars = 'Country/Region', var_name='state', value_name='value')

#print("here hree here")

#print(COVID19_US_cases_new_transpose.head())

#COVID19_US_cases_new_transpose = COVID19_US_cases_new_transpose.drop(['American Samoa','Diamond Princess'], axis=1)

#COVID19_US_cases_new_transpose = COVID19_US_cases_new_transpose.columns.values[0] = 'date'

#COVID19_US_cases_new_transpose = COVID19_US_cases_new_transpose.rename(columns={"Province_State" : "date", "Alabama" : "shit_hole"})

COVID19_US_cases_melt = COVID19_US_cases_transpose.melt(id_vars= 'index', var_name='State', value_name='cases')

print(COVID19_US_cases_melt)

COVID19_US_cases_melt['ratio'] = 1
COVID19_US_cases_melt['new_cases'] = 0

for index, row in COVID19_US_cases_melt.iterrows():
    if((COVID19_US_cases_melt.loc[index]['cases'] == 0) or (COVID19_US_cases_melt.loc[index-1]['cases'] == 0)):
        COVID19_US_cases_melt.loc[index,'ratio'] = 1
    else:
        COVID19_US_cases_melt.loc[index,'ratio'] = COVID19_US_cases_melt.loc[index]['cases']/COVID19_US_cases_melt.loc[index-1]['cases']
        COVID19_US_cases_melt.loc[index,'new_cases'] = COVID19_US_cases_melt.loc[index]['cases'] - COVID19_US_cases_melt.loc[index-1]['cases']
        Cases_1 = COVID19_US_cases_melt.loc[index,'ratio']
        Cases_2 = COVID19_US_cases_melt.loc[(index-1),'ratio']
        Cases_3 = COVID19_US_cases_melt.loc[(index-2),'ratio']       
        COVID19_US_cases_melt.loc[index,'ratio'] = (Cases_1 + Cases_2 + Cases_3) / 3

COVID19_US_cases_melt = COVID19_US_cases_melt.rename(columns={"index" : "date"})

COVID19_US_cases_melt.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_cases_melt.csv', index = False)

#move on to the deaths spreadsheet


COVID19_US_deaths = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_deaths_US.csv')

COVID19_US_deaths_new = COVID19_US_deaths.drop(['Population','UID','iso2','iso3','code3','FIPS','Admin2','Country_Region','Combined_Key','Lat','Long_'], axis=1)

print(COVID19_US_deaths_new)

#COVID19_US_deaths_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_deaths_new.csv',index=False)

COVID19_US_deaths_sum = COVID19_US_deaths_new.groupby(['Province_State']).sum()

#COVID19_US_deaths_new_sum.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_deaths_new_sum.csv')

COVID19_US_deaths_transpose = COVID19_US_deaths_sum.T.reset_index()

#COVID19_US_deaths_new_transpose = COVID19_US_deaths_new_transpose.drop(['American Samoa','Diamond Princess'], axis=1)

#print(COVID19_US_deaths_new_transpose)

#COVID19_US_deaths_new_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_deaths_new_transpose.csv')

COVID19_US_deaths_melt = COVID19_US_deaths_transpose.melt(id_vars= 'index', var_name='state', value_name='deaths')

COVID19_US_deaths_melt['ratio'] = 1

for index, row in COVID19_US_deaths_melt.iterrows():
    if((COVID19_US_deaths_melt.loc[index]['deaths'] == 0) or (COVID19_US_deaths_melt.loc[index-1]['deaths'] == 0)):
        COVID19_US_deaths_melt.loc[index,'ratio'] = 1
    else:
        COVID19_US_deaths_melt.loc[index,'ratio'] = COVID19_US_deaths_melt.loc[index]['deaths']/COVID19_US_deaths_melt.loc[index-1]['deaths']
        Cases_1 = COVID19_US_deaths_melt.loc[index,'ratio']
        Cases_2 = COVID19_US_deaths_melt.loc[(index-1),'ratio']
        Cases_3 = COVID19_US_deaths_melt.loc[(index-2),'ratio']
        COVID19_US_deaths_melt.loc[index,'ratio'] = (Cases_1 + Cases_2 + Cases_3) / 3

COVID19_US_deaths_melt = COVID19_US_deaths_melt.rename(columns={"index" : "date"})

print(COVID19_US_deaths_melt)

COVID19_US_deaths_melt.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_deaths_melt.csv', index = False)

