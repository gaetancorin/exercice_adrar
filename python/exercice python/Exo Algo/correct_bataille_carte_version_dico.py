import random

#Création du deck de base
deck = {"As":14, "deux":2, "trois":3, "quatre":4, "cinq":5, "Valet":11, "Dame":12, "Roi":13}

#Initialisation du deck des joueurs

j1 = {'pique':[], 'coeur':[], 'carreau':[], 'trefle':[]}
j2 = {'pique':[], 'coeur':[], 'carreau':[], 'trefle':[]}

couleur = ["pique","coeur","carreau","trefle"]
#Remplissage du deck du joueur 1 avec les 52 cartes
for i in couleur:
    for carte in deck:
        if i in j1:
            j1[i].append((carte, deck[carte]))
        else:
            j1[i] = [(carte, (deck[carte]))]
print(j1)
input()
#Répartition des 52 cartes entre les deux decks
for i in couleur:
    for k in range(4):
        card = random.randint(0, len(j1[i]) - 1)
        j2[i].append(j1[i][card])
        j1[i].pop(card)
print(j1,j2)
input()
#Initialisation des variables necessaires au jeu
score_j1 = 0
score_j2 = 0
gagne = False

#Boucle de jeu
while not gagne:
    #Choix couleur 1
    couleur1 = random.choice(couleur)
    #Cas ou le joueur 1 n'a plus de cartes de la couleur1
    while len(j1[couleur1]) == 0:
        couleur1 = random.choice(couleur)

    couleur2 = random.choice(couleur)
    while len(j2[couleur2]) == 0:
        couleur2 = random.choice(couleur)

    #Choix de la carte de la couleur1
    carte1 = random.randint(0, len(j1[couleur1])-1)
    print("le joueur 1 a tiré la carte : {} de {}".format(j1[couleur1][carte1][0], couleur1))
    j1 = {"pique":[("As", 14),("deux",2)]}
    carte2 = random.randint(0, len(j2[couleur2])-1)
    print("le joueur 2 a tiré la carte : {} de {}".format(j2[couleur2][carte2][0], couleur2))


    #Comparaison de la force de chaque carte tiré
    if j1[couleur1][carte1][1] > j2[couleur2][carte2][1]:
        print("le joueur 1 gagne")
        score_j1 += 1
    else:
        print("le joueur 2 gagne")
        score_j2 += 2

    #Supression de la carte dans chaque deck
    j1[couleur1].pop(carte1)
    j2[couleur2].pop(carte2)

    #Condition de fin du jeu
    
    if len(j1["pique"]) == 0 and len(j1["coeur"]) == 0 and len(j1["carreau"]) == 0 and len(j1["trefle"]) == 0:
        gagne = True


print("joueur 1 gagne" if score_j1 > score_j2 else "joueur 2 gagne")