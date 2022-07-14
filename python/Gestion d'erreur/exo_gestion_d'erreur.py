
# Réalisez un programme qui demande à l’utilisateur un
# nombre de notes à inscrire, puis les valeurs de ces notes.
# Ces valeurs seront enregistrés dans un tableau. Le
# programme affichera :
# - la meilleure note
# - la pire note
# - la moyenne des notes


recommencer = True
while recommencer:
    nbrNotes = input("Indiquez le nombre de notes à enregistrer\n")
    try:
        nbrNotes = int(nbrNotes)
    except Exception as e:
        print("Désolé, je n'ai compris votre chiffre, veuillez indiquer un chiffre et non des lettres.")
        print(e)
    else:
        recommencer = False