import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
import csv

df1 = pd.read_csv('Master_Dependency.csv', skipinitialspace=True)
df2 = pd.read_csv('App_Dependency_list.csv', skipinitialspace=True)

def format_df(data):
    for col in data.columns:
        # check if the columns contains string data
        if pd.api.types.is_string_dtype(data[col]):
            data[col] = data[col].str.strip()
            data[col] = data[col].str.lower()
    df = data.replace({"":np.nan}) # if there remained only empty string "", change to Nan
    return data

df1 = format_df(df1)
df2 = format_df(df2)

'''
Method 1 : isin method/function

result = df2[~df2.apply(tuple,1).isin(df1.apply(tuple,1))]
result2 = df1[~df1.apply(tuple,1).isin(df2.apply(tuple,1))]
'''

'''
Method 2 : merge method
'''

if DataFrame.equals(df1,df2):
    print(
    '''Same - No need to find delta.
       Start updating pom.xml''')
else:
    print("*"*90)
    result3 = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge'] != 'both']
    #result3 = df1.merge(df2, indicator=True) To find common dependency in both.
    result3.pop('_merge')
    print(result3)
    result3.to_csv('app_dep_delta.csv', index=False)

#Use mode='a' to use append
#result3 = result3.drop([first_column], axis=1)

