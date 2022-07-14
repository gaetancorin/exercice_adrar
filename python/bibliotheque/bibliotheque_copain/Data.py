from BDClass import BD
from BibliothequeClass import Bibliotheque
from LivreClass import Livre
from PersonneClass import Personne
from UserClass import User

#crée et renvoi une liste de livre préfaite
#ne prend aucun argument
#retourne une liste d'objet livre
def DataLivre():
    livre_a = Livre("One Piece", "Eiichiro Oda", "Français", "Aventure", "Manga", "OE125963" ,"2")
    livre_b = Livre("Demon Slayer", "Koyoharu Gotouge", "Français", "Fantastique", "Manga", "DK365964" ,"2")
    livre_c = Livre("Les Misérables", "Victor Hugo", "Français", "Drame", "Roman", "MV864023","4")
    livre_d = Livre("Monsieur Étonnant", "Roger Hargreaves", "Français", "Humour", "Bande dessiné", "MR546987","1")
    livre_e = Livre("Wheel of Time", "Robert Jordan et Brandon Sanderson", "Anglais", "Fantastique", "Roman", "WR147258", "4")
    livre_f = Livre("Shinning", "Stephen King", "Italien", "Horreur", "Roman", "SS569321", "3")
    livre_g = Livre("Demi-vie", "Eric Lafon", "Français", "Horreur", "Roman", "DE842674", "2")
    resultat = [livre_a, livre_b, livre_c, livre_d, livre_e, livre_f]
    return resultat

#crée et renvoi une Bibliothque préfaite
#ne prend aucun argument
#retourne un objet de type Bibliotheque
def DataBibliotheque():
    biblio_a = Bibliotheque("bibliotheque de Purpan", [], [], [], [])
    biblio_b = Bibliotheque("bibliotheque de Blagnac", [], [], [], [])
    les_biblio = [biblio_a, biblio_b]

    return les_biblio

#crée et renvoi une liste de Personne préfaite
#ne prend aucun argument
#retourne une liste contenant des objet de type Personne
def DataPersonne():
    personne_a = Personne("przybylo.m", "przybylo", "maxime", "Fan2Devops")
    personne_b = Personne("morin.j", "morin", "jordan", "DevMieuxQueOps")
    personne_c = Personne("cannapin.g", "cannapin", "gogulavasan", "LaForceDeLamitier")
    personne_d = Personne("dietrich.k", "dietrich", "kheandee", "OneMillionKamas")
    personne_e = Personne("mendouga.a", "mendouga", "adeline", "FemiNazi")
    personne_f = Personne("lafon.e", "lafon", "eric", "FlipReset")
    personne_g = Personne("soulier.r", "soulier", "romain", "OuSontMesMeubles?")
    personne_h = Personne("esteban.d", "esteban", "david", "CallMeACE")
    personne_i = Personne("nozet.t", "nozet", "teddy", "OuiPoulet")
    personne_j = Personne("valero.j", "valero", "johan", "StephaneBerne")
    personne_k = Personne("corin.g", "corin", "gaetan", "Crouton")
    personne_l = Personne("tomps.f", "tomps", "florent", "SMAAAAASH")
    personne_m = Personne("thomas.r", "thomas", "prenom", "Chocoblasted")
    ma_liste_de_personnes = [personne_a]
    return ma_liste_de_personnes