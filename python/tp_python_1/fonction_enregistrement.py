def categorie_age(annee):
    age = 2022 - int(annee)
    if age < 6 or age > 40:
        return "Non_admis"
    elif age < 12:
        return "Poussin"
    elif age < 18:
        return "Cadet"
    elif age < 24:
        return "Junior"
    elif age < 30:
        return "Semi_pro"
    elif age <= 40:
        return "Pro"


def adresse_email(nom,prenom):
    a = str(prenom[0]+"."+nom+"@baton-rouge.fr")
    return a
