#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:06:52 2018

@author: buckz
"""

thelist = ['chaud', 'froid', 'tempéré', 'glacial', 'brûlant']
file = open('temperature.txt', 'w+')

for item in thelist:
  file.writelines(str(item) + "\n")

b = file.readline()
print(b)

file.close()