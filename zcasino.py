from random import randrange
from math import ceil

argent = 25
continuer_partie = True

print("Vous vous installez à la table de roulette avec", argent, "$.")

while continuer_partie:
    nb_mise = -1
    while nb_mise < 0 or nb_mise > 49:
        nb_mise = input("Tapez le nombre sur lequel vous voulez miser (0 à 49) : ") 
        try:
            nb_mise = int(nb_mise) 
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nb_mise < 0:
            print("Ce nombre est négatif")
        if nb_mise > 49:
            print("Ce nombre est supérieur à 49")
        
            
    mise = 0
    
    while mise <= 0 or mise > argent:
        mise = input("Tapez le montant de votre mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")
        
    nb_win = randrange(50)
    print("La roulette tourne et s'arrête .. sur le ", nb_win)
    
    if nb_win == nb_mise:
        print("Félicitations ! Vous obtenez", mise * 3, "$ !")
        argent += mise * 3
    elif nb_win % 2 == nb_mise % 2:
        mise = ceil(mise * 0.5)
        print("Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
        argent += mise
    else:
        print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
        argent -= mise
        
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False

    else:
        print("Vous avez à présent", argent, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")

        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False


