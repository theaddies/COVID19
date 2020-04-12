import pandas as pd

df = pd.read_csv (r'C:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_US.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print (len(df))
print(df.describe())
print(df)

df_new = df.drop(['UID','iso2','iso3','code3','FIPS','Admin2','Country_Region','Combined_Key','Lat','Long_'], axis=1)

print(df_new)

df_new.to_csv(r'c:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\df_new.csv',index=False)

df_new_sum = df_new.groupby(['Province_State']).sum()

df_new_sum.to_csv(r'c:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\df_new_sum.csv')

df_new_transpose = df_new_sum.T

print(df_new_transpose)

df_new_transpose.to_csv(r'c:\Users\thead\Documents\COVID-19\csse_covid_19_data\csse_covid_19_time_series\df_out_transpose.csv')

