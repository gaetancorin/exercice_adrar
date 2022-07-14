# import UserClass

class Personne:
    def __init__(self, id, nom, prenom, mdp):
        self._id = id
        self._nom = nom
        self._prenom = prenom
        self._mdp = mdp

    def __repr__(self):
        return f"Id: {self._id}"

    """
        Argument : Aucun
        retour : String
        description : Retourne une ligne de donnée prête à la sauvegarde
    """
    def ligneDeDonnee(self):
        return f"False;{self._id};{self._nom};{self._prenom};{self._mdp}"

    """
        Argument : Aucun
        retour : String
        description : Imprime les infos d'un compte
    """
    def afficherStatutCompte(self):
        print(f"Voici les infos de votre compte {self.getId()} :")
        print(f"-----------------------")

        if isinstance(self, Personne):
            print("Vous nêtes abonné à aucun programme")


    def getId(self):
        return self._id

    # def estUnUtilisateur(self):
    #     if isinstance(self, UserClass.User):
    #         return True
    #     else:
    #         return False

    def getNom(self):
        return self._nom

    def getPrenom(self):
        return self._prenom

    def getMdp(self):
        return self._mdp

    """
        Argument : test, String
        retour : Bool
        description : indique si le mot de passe indiqué correspond à celui de l'utilisateur
    """
    def verifierMotDePasse(self, test):
        if test == self._mdp:
            return True
        else:
            return False
        
    def changerMotDePasse(self, nvo_mdp):
        self._mdp = nvo_mdp

    def DEBUG_print(self):
        resultat = f'Attribut nom : \n{self._nom}\n\n AttributPrénom: {self._prenom}\n\n Attribut Id:\n{self._id}'
        return resultat