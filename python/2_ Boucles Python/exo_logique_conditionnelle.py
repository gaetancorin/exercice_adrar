# Réaliser un programme qui demande un nombre à un
# utilisateur et qui lui dira si le nombre est pair ou impair

nb = int(input("indiquez un nombre\n"))

if nb == 0:
    print("0 n'est ni pair ni impair")
elif nb%2 == 0:
    print("nombre pair")
else:
    print("nombre impair")

# Réalisez un programme qui demandera à l’utilisateur son
# jour, mois et année de naissance et qui indiquera si il est
# majeur ou non.

jour = int(input("indiquez votre jour de naissance (le chiffre)"))
mois = int(input("indiquez le chiffre de votre mois de naissance (3 pour mars par exemple"))
annee = int(input("indique votre annee de naissance"))

if annee > 2021-18:
    print("vous n'etes pas majeur")
elif mois > 12:
    print("vous n'etes pas majeur")
elif mois == 12 and jour > 16:
    print("vous n'etes pas majeur")
else:
    print("vous etes majeur")

if (annee > 2021-18) or (annee > 2021-18 and mois == 12 and jour > 16):
    print("vous n'etes pas majeur")
else:
    if annee == 2021-18 and jour == 16 and mois == 12:
        print("bon anniversaire")
    print("vous etes majeur")

# Réalisez un programme qui demande à l’utilisateur le
# nombre d’articles, puis le prix hors taxes de chaque article
# et qui affichera le prix total TTC

nb = int(input("indiquez le nombre d'article à scanner\n"))
i = 1
HT = 0
TVA = 0.2
#
# while i <= nb:
#     print("Indiquez le prix de l'article numero", i)
#     HT += int(input())
#     i += 1

for j in range(1, nb+1):
    print("Indiquez le prix de l'article numero", j)
    HT += int(input())

print("Votre total TTC est de", HT*(1+TVA), "€")
