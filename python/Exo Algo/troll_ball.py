import random

equipe1 = input("quel est le nom de l'equipe 1 \n")
equipe2 = input("quel est le nom de l'equipe 2 \n")

dico1 = {equipe1: 20 ,equipe2: 20}

while dico1[equipe1] != 0 and dico1[equipe2] != 0:
    perdant_tour = random.randint(1, 2)
    if perdant_tour == 1:
        dico1[equipe1] -= 1
    else:
        dico1[equipe2] -= 1
    print(dico1)

if dico1[equipe1] == 0:
    print(f"fin du match, {equipe2} a gagné")
else:
    print(f"fin du match, {equipe1} a gagné")
