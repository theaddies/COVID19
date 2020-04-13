import pandas as pd
#confirmed cases spreadsheet

COVID19_test = pd.read_csv (r'C:\Users\thead\Documents\bootcamp\COVID19_out\test.csv')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"

print("index1")
print(COVID19_test.index)
print(COVID19_test)
COVID19_test = COVID19_test.rename(columns={"Country/Region" : "date"})

print(COVID19_test)

#COVID19_test_transpose = COVID19_test.set_index('date').T

COVID19_test_transpose = COVID19_test.T

print("index2")
print(COVID19_test_transpose.index)

#COVID19_test_transpose = COVID19_test_transpose['date'].astype('datetime64')

#COVID19_global_test_transpose = COVID19_test.T

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.droplevel(level=0)

#COVID19_global_cases_new_transpose = COVID19_global_cases_new_transpose.drop(['Guam','Northern Mariana Islands','American Samoa','Diamond Princess','Grand Princess'], axis=1)
print("here")
print(COVID19_test_transpose.head())

print(COVID19_test_transpose.index)

print(COVID19_test_transpose.dtypes)

#COVID19_test_transpose = COVID19_test_transpose.astype('datetime64')

print(COVID19_test_transpose)

#COVID19_test_transpose.head().to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_test_new_head.csv')

COVID19_test_transpose.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_test_new_transpose.csv')

COVID19_test_melt = pd.melt(COVID19_test_transpose, col_level=0, id_vars=[0])

print(COVID19_test_melt)

COVID19_test_melt.to_csv(r'c:\Users\thead\Documents\bootcamp\COVID19_out\COVID19_test_melt.csv')