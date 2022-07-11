def ecrire(fichier):
    with open(fichier, "w") as fic:
        for i in range(5):
            fic.write("abcdef\n")
            fic.write("123456\n")

def analyse_ligne(fichier):
    with open(fichier, "r") as fic:
        for line in fic:
            if line[:-1].isalpha():
                print("mots")
            else:
                print("nombres")

ecrire("test3.txt")
analyse_ligne("test3.txt")