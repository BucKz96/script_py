#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:32:05 2018

@author: buckz
"""

import pandas as pd

file = '/home/buckz/Data/sante.txt'
df = pd.read_table(file, sep='|')
df=df.dropna(axis=1,how='all')
writer = '/home/buckz/Data/sante.xls'
df.to_excel(writer)

#idx = 8
#new_col = ["patient1", "patient2", "patient3"]
#df.insert(loc=idx, column='patient_id', value=new_col)
df['patient_id'] = pd.Series(["patient1", "patient2", "patient3"])

df.set_index(['patient_id'], inplace=True)

def delete_na(df_entry):
    if df_entry.empty == True:
        print('Your Dataframe is empty')
    else:
        dataframe = dataframe.dropna(axis=1, how='all')
        dataframe = dataframe.dropna(axis=0, how='all')

delete_na(df)
                

