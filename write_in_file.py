
f = open('text.txt', 'w')
ligne = ('Ceci est ma ligne : ')
for i in range(1, 11):
    f.write(ligne + str(i) + '\n')
f.close()



    
    
    