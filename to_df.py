#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:12:16 2018

@author: buckz
"""
import pandas as pd
import urllib


url = ""
with open('/home/romain/DATA/test.txt', 'r') as test:
    test.write(urlopen(url).read())

def my_read_table(file, sep=','):
    import warnings
    warnings.filterwarnings("error")
    try:
        df = pd.read_table(file, sep)
        print('Lecture normale effectuée')
        print('les dimensions du dataframe sont : {} lignes par {} colonnes\n'.format(df.shape[0], df.shape[1]))
        print(df.head())
        print(df.tail())
        return (df)
    except pd.errors.DtypeWarning:
        df= pd.read_table(file, sep, low_memory=False)
        print('Lecture du fichier / mode volumineux')
        print('les dimensions du dataframe sont : {} lignes par {} colonnes\n'.format(df.shape[0], df.shape[1]))
        print(df.head())
        print(df.tail())
        return (df)
    except FileNotFoundError:
        print('Ce fichier est introuvable')
    except pd.errors.EmptyDataError:
        print('Ce fichier ne permet pas de constituer un DataFrame')
    except ValueError:
        print("Votre séparateur annoncé n'est pas valide")
    finally:
        warnings.filterwarnings("error")
    
df = Checkfile('sante.txt', '|')
        
    

df_obj = df.select_dtypes(include=['object']).copy()
df_obj.describe()

for col in df_obj.columns:
    num_unique_values = len(df_obj[col].unique())
    num_total_values = len(df_obj[col])
    if num_unique_values / num_total_values < 0.5:
        df.loc[:,col] = df_obj[col].astype('category')
    else:
        df.loc[:,col] = df_obj[col]

def change_name(name) : 
   return name.strip().lower().replace(' ','_')

df.columns  =  [change_name(x) for x in df.columns]