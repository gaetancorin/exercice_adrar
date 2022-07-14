def multiplier(nbr1, nbr2):
    return nbr1*nbr2

nb1,nb2 = input("indiquez deux nombres séparés par des espaces\n").split(" ")

nb1 = int(nb1)
nb2 = int(nb2)

# autre facon de transformer nb1 et nb2 en int
# nb1,nb2 = [int(x) for x in input("indiquez deux nombres séparés par un espace\n").split(" ")]

print("{} x {} = {}".format(nb1,nb2,multiplier(nb1,nb2)))