import random

equipe1, equipe2 = input("indiquez le nom des équipes (séparés par un espace)\n").split()

scores = {equipe1:5, equipe2:5}
i = 0

while scores[equipe1] != 0 and scores[equipe2] != 0:
    print("Tour numéro {} : \n{} : {} pts\n{} : {} pts".format(i, equipe1, scores[equipe1], equipe2, scores[equipe2]))

    perdant = random.randint(1, 2)
    if perdant == 1:
        scores[equipe1] -= 1
    else:
        scores[equipe2] -= 1
    i += 1
    input("lancez le tour suivant (touche entrée)")
    
if scores[equipe1] == 0:
    print("le grand gagnant est :", equipe2)
else:
    print("le grand gagnant est:", equipe1)