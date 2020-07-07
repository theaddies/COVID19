# -*- coding: utf-8 -*-
"""
Created on Mon May 18 08:36:44 2020

@author: theaddies
"""
path = 'https://covidtracking.com/api/v1/states/daily.json'
import num
import pandas as pd

df = pd.read_json(path)

print(df)