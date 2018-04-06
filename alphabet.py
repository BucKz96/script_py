#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:24:33 2018

@author: buckz
"""

def alpha():
    answer = input('Rentre ta lettre pour connaître la suivante : ')
    answer = answer.lower()
    answer = answer.strip()
    if len(answer) > 1:
        print('Degage, tu as mis plusieurs charac')
        return
    if not answer.isalpha():
        print('Tu n\'a pas rentré un charac')
        return
    try:
        answer_next = int(input('Quel pas veux-tu ? : '))
    except:
        print('Tu fais n\'importe quoi')
    else:
        nb = ord(answer) - 97;
        print(chr(((nb + answer_next) % 26) + 97))
alpha()