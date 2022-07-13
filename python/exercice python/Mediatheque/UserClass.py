from PersonneClass import Personne
from datetime import timedelta, date
import Rules

class User(Personne):
    def __init__(self, identifiant, nom, prenom, mdp, grade = Rules.defautGrade()):
        super().__init__(identifiant, nom, prenom, mdp)
        self._emprunts = {}
        self._grade = grade

    """
        Argument : Aucun
        retour : String
        description : Retourne une ligne de donnée prête à la sauvegarde
    """
    def ligneDeDonnee(self):
        return f"True;{self._id};{self._nom};{self._prenom};{self._mdp};{self._grade};{self._emprunts}"

    """
        Argument : book, Livre
        retour : None
        description : Ajoute un emprunts à la liste des emprunts utilisateur
    """
    def ajouterEmprunt(self, book):
        taille = book.getTaille()
        end = date.today() + timedelta(days=taille * 7)
        self._emprunts[book.getReference()] = end

    """
        Argument : reference, String ; jours_supplementaires, Integer
        retour : None
        description : allonge la durée d'un emprunt
    """
    def allongerEmprunt(self, reference, jours_supplementaires):
        self._emprunts[reference] = self._emprunts[reference] + timedelta(days=jours_supplementaires)

    """
        Argument : Aucun
        retour : dict<>
        description : retourne le dictionnaire des emprunts, avec comme clé la référence, et comme valeur la date de retour prévue 
    """
    def getEmprunts(self):
        return self._emprunts

    """
        Argument : Aucun
        retour : Integer
        description : Retourne le nombre d'emprunt toujours en cours
    """
    def nombreEmpruntEnCours(self):
        return len(self._emprunts)

    """
        Argument : book, Livre
        retour : Integer
        description : Retourne le nombre d'emprunt toujours en cours
    """

    def initEmprunt(self, emprunts):
        self._emprunts = emprunts

    def rendreLivre(self, book):
        self._emprunts.pop(book.getReference())

    def getGrade(self):
        return self._grade

    def getMaxEmprunt(self):
        return self._grade["Max Emprunts"]

    

    def afficherStatutCompte(self):
        # super().afficherStatutCompte()
        print(f'Votre grade : {self._grade["Nom formule"]} - {self._grade["Max Emprunts"]} emprunts max')
        print(f"-----------------------")
        if len(self._emprunts) > 0:
            print("\nVoici la liste des emprunts :\n")
            for i, j in self._emprunts.items():
                print(f"{i} - à rendre avant {j}")
        else:
            print("Vous n'avez aucun emprunts en cours")

    def changerGrade(self, value):
        pass
    
    def __repr__(self):
        return f'Nom: {self._nom}\nPrénom: {self._prenom}\nFormule souscris:{self._grade["Nom formule"]}'

    def DEBUG_print(self):
        resultat = f'Attribut nom : \n{self._nom}\n\n AttributPrénom: {self._prenom}\n\n Attribut Id:\n{self._id}\n\nAttribut Formule:\n{self._grade}\n\nAttribut Emprunts: \n{self._emprunts}'
        return resultat