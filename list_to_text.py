#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:14:55 2018

@author: buckz
"""

thelist = ['Maxime', 'Kevin', 'Laura', 'Romain', 'Nassim & Facebook', 1]
file = open('list.txt', 'w+')

for item in thelist:
  file.write(str(item) + "\n")

b = file.readline()
print(b)

file.close()


