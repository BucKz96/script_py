import random

def guess_num():
    
    var_alea = random.randrange(0, 10, 1)
    player_choice = -1
    nb_try = 0
    nb_try_max = 3

    while player_choice != var_alea and nb_try <= nb_try_max:
        player_choice = int(input("Devine le nombre auquel je pense qui est compris entre 0 et 10\n"))
        if var_alea > player_choice:
            print("c'est trop petit\n")
        elif var_alea < player_choice:
            print("c'est trop grand\n")
        elif var_alea == player_choice:
            print("You Win !")
        nb_try+=1
        elif nb_try == nb_try_max:
            print("Perdu !")
            break
    print("nombre d'essais :\n", nb_try)
    
guess_num()
