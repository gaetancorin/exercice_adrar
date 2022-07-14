
# Réalisez un programme qui demandera à l’utilisateur son
# nom, son prénom et son année de naissance et qui
# affichera « Bonjour prénom nom , vous avez age ans ».

prenom= input("Quel est votre prénom? \n")
nom= input("quel est votre nom? \n")
date= int(input("Quel est votre année de naissance? \n"))
print("Bonjour", prenom, nom, "vous avez", 2021-date,"ans")

# Réalisez un programme qui demande 3 nombres à
# l’utilisateur et qui affiche la somme des 3 (accordez de
# l’importance au formatage de l’affichage)

var1 = int(input("donne un nombre \n"))
var1 += int(input("un autre stp \n"))
var1 += int(input("encore un ! \n"))
print ("Abracadabra j'additionne et ça donne ce résultat:", var1)


# Réalisez un programme qui demande un nombre à
# l’utilisateur et qui affiche le cube de ce nombre sans créer
# de nouvelle variable.

var2 = int(input("donne un nombre \n"))
print ("Voila le résultat puissance 3!", var2**3)


# réalisez un programme qui demande un nombre à un utilisateur
# et qui fais la conversion binaire et en hexa de ce nombre.

var3= int(input("Donne un nombre \n"))
var4= bin(var3)
var5= hex(var3)
print("valeur en binaire", var4, "et la valeur en Hexadecimal", var5)


# réalisez un programme qui affiche les methodes d'un type
# d'objet

print("Pour ce qui est des String on a :")
print(dir("Chaine de caractères"))
print("Pour ce qui est des Integer on a :")
print(dir(5))

# réalisez un programme qui demande une phrase à un utilisateur
# et qui affichera la longueur de la phrase

var6= input("Ecrit moi une histoire! \n")
print(len(var6))


# réalisez un programme qui demande 4 nombres à un utilisateur
# et qui affichera la valeur maximum et minimum

a= int(input("1er nombre \n"))
b= int(input("2ème nombre \n"))
c= int(input("3ème nombre \n"))
d= int(input("4ème nombre \n"))
print("valeur min" ,min(a,b,c,d), "valeur max", max(a,b,c,d))




