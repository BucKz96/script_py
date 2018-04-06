#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:30:01 2018

@author: buckz
"""

#//////////// Nombre de mots : 139719 /////////////////

#num_lines = sum(1 for line in open('french.txt'))
#print(num_lines)

#///////////// Mot le plus long : anticonstitutionnellement ///////////// 

#file = open('french.txt', 'r+')
#string = file.read()
#words = []
#max_string = []
#lines = string.split("\n")

#for each in lines:
 #   words += each.split(" ")

#for each in words:
#    if len(each) >= 25:
  #      max_string.append(each)        
#print(max_string)
#file.close()
  
#//////////// Pourcentage de mots contenant un 'e' : 78.54193058925415 /////////////////////

#file = open('french.txt', 'r+')
#nb_e = 0
#for each in file:
    #if 'e' in each:
        #nb_e += 1
#print((nb_e / 139719) * 100)
        
#//////////////////////////// Nombre de mots commençant par 'e' : 8468 ////////////////////////////

#file = open('french.txt', 'r+')
#nb_start_e = 0

#for each in file:
    #if each[0] == 'e':
        #nb_start_e += 1

#print(nb_start_e)

#//////////////////////////// Mots contenant 'th' suivi d'une consomne : 109 ///////////////////////////

#import re

#file = open('french.txt', 'r+')
#nb_th_cons = 0
#expression = r"^.*th[bcdfghjklmnpqrstvwxz].*$"

#for each in file:
    #if re.match(expression, each):
        #nb_th_cons += 1
#print(nb_th_cons)

#/////////////////////////// 7eme lettre la plus fréquente : 'e' //////////////////////////////
        
import operator        
        
with open('french.txt', 'r+') as file:    
    nb_letter = {}
    for each in file:
        try:
            letter = each[6]
            nb_letter[letter] = nb_letter.get(letter, 0) + 1
        except IndexError:
            None

sorted_dict = sorted(nb_letter.items(), reverse=True, key=operator.itemgetter(1))
print(sorted_dict)     
    
    



    