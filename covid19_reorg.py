import pandas as pd
#confirmed cases spreadsheet

COVID19_US_cases = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
#print (len(df))
#print(df.describe())
#print(df)

COVID19_US_cases_new = COVID19_US_cases.drop(['UID','iso2','iso3','code3','FIPS','Admin2','Country_Region','Combined_Key','Lat','Long_'], axis=1)

print(COVID19_US_cases_new)

COVID19_US_cases_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_cases_new.csv',index=False)

COVID19_US_cases_new_sum = COVID19_US_cases_new.groupby(['Province_State']).sum()

COVID19_US_cases_new_sum.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_cases_new_sum.csv')

COVID19_US_cases_new_transpose = COVID19_US_cases_new_sum.T

print("here hree here")

print(COVID19_US_cases_new_transpose.head())

#COVID19_US_cases_new_transpose = COVID19_US_cases_new_transpose.drop(['American Samoa','Diamond Princess'], axis=1)

#COVID19_US_cases_new_transpose = COVID19_US_cases_new_transpose.columns.values[0] = 'date'

COVID19_US_cases_new_transpose = COVID19_US_cases_new_transpose.rename(columns={"Province_State" : "date", "Alabama" : "shit_hole"})

print(COVID19_US_cases_new_transpose)

COVID19_US_cases_new_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_cases_new_transpose.csv')

#move on to the deaths spreadsheet


COVID19_US_deaths = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_deaths_US.csv')

COVID19_US_deaths_new = COVID19_US_deaths.drop(['Population','UID','iso2','iso3','code3','FIPS','Admin2','Country_Region','Combined_Key','Lat','Long_'], axis=1)

print(COVID19_US_deaths_new)

COVID19_US_deaths_new.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_deaths_new.csv',index=False)

COVID19_US_deaths_new_sum = COVID19_US_deaths_new.groupby(['Province_State']).sum()

COVID19_US_deaths_new_sum.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_deaths_new_sum.csv')

COVID19_US_deaths_new_transpose = COVID19_US_deaths_new_sum.T

COVID19_US_deaths_new_transpose = COVID19_US_deaths_new_transpose.drop(['American Samoa','Diamond Princess'], axis=1)

print(COVID19_US_deaths_new_transpose)

COVID19_US_deaths_new_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_US_deaths_new_transpose.csv')