# code crée par rayan belhamra
# 2022-10-21
#tp2


import random

x = random.randint(0,100)
nb_essai = 0
print("j'ai choisi un nombre entre 0 et 100 ")
guess = -1
while (guess != x):
    guess=int(input("entrez votre essai"))
    nb_essai += 1
    if guess < x:
        print("votre chiffre est plus petit que celui qu'on cherche ")
    elif guess > x:
        print("votre chiffre est plus grand que celui qu'on cherche")