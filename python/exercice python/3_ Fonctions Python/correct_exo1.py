def calcul_age(annee):
    return 2022 - annee


continuer = True
while continuer:
    year = input("indiquez votre année de naissance\n")
    try:
        year = int(year)
    except ValueError:
        print("veuillez indiquer l'année en chiffres")
    else:
        continuer = False

print(f"vous avez {calcul_age(year)} ans")