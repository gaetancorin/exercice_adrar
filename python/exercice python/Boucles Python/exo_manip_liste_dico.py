



# Réalisez un programme qui demande à l’utilisateur un
# nombre de notes à inscrire, puis les valeurs de ces notes.
# Ces valeurs seront enregistrés dans un tableau. Le
# programme affichera :
# - la meilleure note
# - la pire note
# - la moyenne des notes

# -------------------------------------------------------------------------------------
# Exercice liste de notes : première correction
nb_notes = int(input("indiquez le nombre de notes\n"))
liste_notes = []
somme = 0
maxi = 0
mini = 20
for i in range(nb_notes):
    note = int(input("indiquez une note\n"))
    liste_notes.append(note)
    somme += note
moyenne = somme / nb_notes

for i in liste_notes:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print("la note maximale est:", max(liste_notes), "et la note minimale est:", min(liste_notes))
print("votre moyenne est de:", sum(liste_notes)/nb_notes)
print("la note maximale est:", maxi, "et la note minimale est:", mini)
print("votre moyenne est de:", moyenne)

# -----------------------------------------------------------------------------------------
# Exercice liste de notes : deuxième correction

# dico = {}
# dico['cle'] = 'valeur'

nbrNotes = int(input("Indiquez le nombre de notes à enregistrer\n"))

notes = {}
maxi = 0
mini = 20
matMax = ""
matMin = ""

for i in range(nbrNotes):
    mat = input("indiquez la matière\n")
    val = int(input("indiquez la note de cette matière\n"))
    enregistrement = {mat: val}
    notes.update(enregistrement)
    #notes[mat] = val

for i in notes:
    print(i, notes[i], sep=" : ")

# for i in notes:
#     if notes[i] > maxi:
#         maxi = notes[i]
#         matMax = i
#     if notes[i] < mini:
#         mini = notes[i]
#         matMin = i

print("la note maximale est: {} et c'est la matiere {}. La note minimale est {} et c'est la matiere {}".format(maxi, matMax, mini, matMin))
moyenne = sum(notes.values()) / nbrNotes
print("votre moyenne est de : {}/20".format(moyenne))
maxi = max(notes.values())
mini = min(notes.values())


matMax = list(notes.keys())[list(notes.values()).index(maxi)]
matMin = list(notes.keys())[list(notes.values()).index(mini)]

print(matMax,maxi, sep=" : ")
print(matMin,mini, sep=" : ")