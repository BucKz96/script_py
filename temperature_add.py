#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:13:31 2018

@author: buckz
"""

thelist = ['hot', 'cold', 'moderate', 'icy', 'ardent']
file = open('temperature.txt', 'a')

for item in thelist:
  file.writelines((str(item) + "\n"))

file.close()