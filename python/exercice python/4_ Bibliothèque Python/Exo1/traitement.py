import donnes

continuer = True
articles = []

while continuer:
    articles.append(int(input("indiquez le prix de l'article\n")))
    rez = input("avez vous un autre article ? y/n\n")
    if rez == "n":
        continuer = False

print("le taux de TVA est de {}%".format(builtin.TVA * 100))

for i in articles:
    print("l'article numéro {} a un prix TTC de {}€".format(articles.index(i)+1, builtin.calcul_ttc(i, builtin.TVA)))

sommeHT = builtin.calcul_total(articles)
sommeTTC = builtin.calcul_ttc(sommeHT, builtin.TVA)
print("vous devez payer {}€".format(sommeTTC))

# print("vous devez payer un total de {} €".format(builtin.calcul_ttc(builtin.calcul_total(tuple(articles)), builtin.TVA)))