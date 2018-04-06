liste_longue = ['a','a','a','b','c','c']
liste_alpha = ['a', 'b', 'c']
liste_desordre = ['b','a','c','c','c','a']

print(liste_longue, liste_alpha, liste_desordre)

decalage = 0
for x in range(0, liste_longue.count("a")) : 
    idx = liste_longue[decalage:].index("a") + decalage 
    print(idx)
    decalage = idx + 1

for indice, value in enumerate(liste_longue) : 
    if 'a' in value : 
        print(indice)


import numpy as np
L = np.array(liste_longue)
indexes, *_  = np.where(L == 'a')