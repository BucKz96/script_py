#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 16:37:15 2018

@author: buckz
"""

import re
user_mail = input('Votre mail : ')
expr = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
while re.search(expr, user_mail) is None:
    user_mail = input('Entrez une adresse mail valide : ')
print('Adresse valide et enregistrée : {}' .format(user_mail))
user_pass = input('Veuillez choisir un mot de passe (4 caractères minimum): ')
expr_pass = "^[a-zA-Z0-9]{4,}$"
while re.search(expr_pass, user_pass) is None:
    user_pass = input('Veuillez choisir un mot de passe qui contient au minimum 4 caractères : ')
print('Mot de passe valide et enregistré : {}' .format(user_pass))
