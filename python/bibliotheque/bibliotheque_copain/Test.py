from UserClass import User
from BibliothequeClass import*
from LivreClass import Livre
from BDClass import BD
from PersonneClass import Personne
import datetime
import Rules as util

num2 = User(44, "pote", "plebe", "test")
num3 = Personne(45, "pote", "plebe", "test2")
lebook1 = Livre("Force", "le Z", "FR", "comedy", "roman", "ZFORCE4", 1, True, None)
lebook2 = Livre("Patrie", "La S", "EN", "Jeunesse", "roman", "ZFFR544", 3, False, None)
lebook4 = Livre("Never", "benjy", "EN", "Jeunesse", "roman", "ZFYTT8", 2, False, None)
lebook3 = Livre("Honneur", "le j", "FR", "cpee", "manga", "DTGRCE4", 2, True, None)
lebook7 = BD("Froid", "le e", "EN", "cpee", "roman", "DTGRDF4", 2, "Michel", True, True, None)

ma_date_de_retour_test = datetime.date.today()
lebook8 = BD("Honneur", "le j", "FR", "cpee", "manga", "DTGRCE4", 2, "Michel", True, False, ma_date_de_retour_test)

biblio = Bibliotheque("bibli_test",[],[],[lebook1,lebook2,lebook3, lebook4, lebook7, lebook8],[num2])

if isinstance(num3, User):
    print("Vrai")
else:
    print("Faux")


# biblio.afficherLivre()
# input()
# biblio.afficherLivreDispo()
# input()
#biblio.afficherLivreGenre()
# biblio.afficherLivreLangue()
# print(biblio)
# print(biblio)

# num2.ajouterEmprunt(lebook1)
# num2.ajouterEmprunt(lebook2)
# num2.ajouterEmprunt(lebook3)

# print("\n\n\n")
# print(num2.getEmprunts())
# print("\n\n\n")

# mes_emprunts = num2.getEmprunts()
# print("la")
# for key in mes_emprunts:
#     print(f"Ref : {key} - à rendre avant le {mes_emprunts[key]}")


# util.voirGrades()
#
#
#
#
ma_recherche = input("Votre recherche : ")
ma_recherche = ma_recherche.upper()
liste_livre_concernes = biblio.rechercher(ma_recherche)
for i in liste_livre_concernes:
    print(i)
    print("\n")
