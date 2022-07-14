import random


deck = []
color = [2,3,4,5,6,7,8,9,10,"Valet","Dames","Roi","As"]
for i in range(4):
    deck.extend(color)

j1 = []
j2 = []
score_j1 = 0
score_j2 = 0
for i in range(26):
    dice1 = random.randint(0, len(deck)-1)
    j1.append(deck[dice1])
    deck.pop(dice1)

    dice1 = random.randint(0, len(deck)-1)
    j2.append(deck[dice1])
    deck.pop(dice1)
while j1 and j2:
    somme = []
    print("joueur 1:",j1[0],"/// nombre de cartes:",len(j1))
    print("joueur 2:",j2[0],"/// nombre de cartes:",len(j2))
    if color.index(j1[0]) > color.index(j2[0]):
        print("gagnant de la manche: joueur 1")
        j1.append(j2[0])
        j1.append(j1[0])
        score_j1 += 1
        j1.pop(0)
        j2.pop(0)
    elif color.index(j1[0]) < color.index(j2[0]):
        print("gagnant de la manche: joueur 2")
        score_j2 += 1
        j2.append(j1[0])
        j2.append(j2[0])
        j1.pop(0)
        j2.pop(0)
    else:
        if len(j1) == 1:
            j2.append(j1[0])
            j1.pop(0)
        elif len(j2) == 1:
            j1.append(j2[0])
            j2.pop(0)
        else:
            while color.index(j1[0]) == color.index(j2[0]) and len(j1) > 1 and len(j2) > 1:
                print("EgalitÃ©")
                somme.append(j1[0])
                somme.append(j2[0])
                j1.pop(0)
                j2.pop(0)
                print("joueur 1:", j1[0],"/// nombre de cartes:",len(j1))
                print("joueur 2:", j2[0],"/// nombre de cartes:",len(j2))
            if color.index(j1[0]) > color.index(j2[0]):
                print("gagnant de la manche: joueur 1. Il gagne {} points".format(len(somme)))
                j1.extend(somme)
                score_j1 += len(somme)
                somme = []
            elif color.index(j1[0]) < color.index(j2[0]):
                print("gagnant de la manche: joueur 2. Il gagne {} points".format(len(somme)))
                j2.extend(somme)
                score_j2 += len(somme)
                somme = []
    print("\n")

print("joueur 1: {} ; joueur 2 : {}".format(score_j1, score_j2))
print("gagnant : joueur 1" if score_j1 > score_j2 else "gagnant : joueur 2")