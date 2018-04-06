nb_user = input("Votre nombre ? : ") # 1 ; &
while isinstance (nb_user, int) == False :
    try : 
        nb_user = int(nb_user)
    except : 
        print("Il semble que vous n'avez pas saisi un nombre entier")
        nb_user = input("Un nombre entier svp ? : ")
        
#while (  nb_user < 0):
#    print("Votre nombre est négatif")
#    input("Un nombre positif svp : ")  
    
if nb_user < 0 :
    while True :
        print("Votre nombre est négatif")
        nb_user = int(input("Un nombre positif svp : "))
        if nb_user > 0:
            print('mnt, votre nb est positif, Merci')
            break
        
