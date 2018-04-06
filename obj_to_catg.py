#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:12:16 2018

@author: buckz
"""
import pandas as pd
import numpy as np

df = pd.read_table('sante.txt')
df_obj = df.select_dtypes(include=['object']).copy()

for col in df_obj.columns:
    num_unique_values = len(df_obj[col].unique())
    num_total_values = len(df_obj[col])
    if num_unique_values / num_total_values < 0.5:
        df.loc[:,col] = df_obj[col].astype('category')
    else:
        df.loc[:,col] = df_obj[col]

df_num = df.select_dtypes(include=['int64']).copy()

for col in df_num.columns:
    df.loc[:,col] = df_num[col].astype(np.int16)
