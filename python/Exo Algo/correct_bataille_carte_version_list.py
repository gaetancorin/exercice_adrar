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
    
print("deck j1:",j1)
print("deck j2:",j2)
input("\n\nLancez le jeu\n")

while j1:#while j1 veut dire : tant qu'il y a des éléments dans j1 (car j1 est une liste)
    print("joueur 1:",j1[0])
    print("joueur 2:",j2[0])
    if color.index(j1[0]) > color.index(j2[0]):
        print("gagnant de la manche: joueur 1")
        score_j1 += 1
    elif color.index(j1[0]) < color.index(j2[0]):
        print("gagnant de la manche: joueur 2")
        score_j2 += 1
    else:
        somme = 1
        while color.index(j1[0]) == color.index(j2[0]) and len(j1) > 1:
            print("Egalité")
            j1.pop(0)
            j2.pop(0)
            somme += 1
            print("joueur 1:", j1[0])
            print("joueur 2:", j2[0])
        if color.index(j1[0]) > color.index(j2[0]):
            print("gagnant de la manche: joueur 1. Il gagne {} points".format(somme))
            score_j1 += somme
        elif color.index(j1[0]) < color.index(j2[0]):
            print("gagnant de la manche: joueur 2. Il gagne {} points".format(somme))
            score_j2 += somme
        else:
            print("Egalité et fin du match")
    j1.pop(0)
    j2.pop(0)
    print("\n")

    
print("---------------")
print("joueur 1: {} \njoueur 2 : {}".format(score_j1, score_j2))
print("gagnant : joueur 1" if score_j1 > score_j2 else "gagnant : joueur 2\n")