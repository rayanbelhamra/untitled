# code crée par rayan belhamra
# 2022-10-21
#tp2


import random

redo = "yes"

# boucle
while redo == ("yes"):

    x = random.randint(0, 100)
    nb_essai = 0
    print("j'ai choisi un nombre entre 0 et 100, et c'est a vous de le deviner ")
    guess = -1
    while (guess != x):
        guess = int(input("entrez votre guess"))
        nb_essai += 1
        # ce qu'on veut que ca print si le nombre
        if guess < x:
            print("votre chiffre est plus petit que celui qu'on cherche ")
        elif guess > x:
            print("votre chiffre est plus grand que celui qu'on cherche")
        elif guess == x:
            print("Vous avez trouver le nombre demandé en " + str(nb_essai) "essais")
    redo = input("Voulez vous quitter?   *repondez par yes ou par no")
print(" thx, bye")
