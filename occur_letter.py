#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:20:45 2018

@author: buckz
"""        

import operator    
texte = "je souhaite compter l'occurence des lettres dans cette phrase"
texte_nospace = texte.replace(" ", "")
nb_letter = {}

for each in texte_nospace:
    nb_letter[each] = nb_letter.get(each, 0) + 1
      
sorted_dict = sorted(nb_letter.items(), reverse=True, key=operator.itemgetter(1))
print(sorted_dict)   