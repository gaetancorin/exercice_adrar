from xml.sax.handler import property_interning_dict


class Bibliotheque:

    def __init__(self, nom, rayons=[], auteurs=[], livres=[], utilisateurs=[]):
        self._nom = nom
        self._rayons = rayons
        self._auteurs = auteurs
        self._livres = livres
        self._utilisateurs = utilisateurs

    """
        Argument : Aucun
        retour : None
        description : Imprime la liste des livres.
    """
    def afficherLivre(self):
        for livre in self._livres:
            print(livre)

    """
        Argument : ref, String
        retour : livre, Livre
        description : Permet d'obtenir un livre via sa référence.
    """
    def obtenirLivre(self, ref):
        for livre in self._livres:
            if livre.getReference().upper() == ref.upper():
                return livre

    """
        Argument : Aucun
        retour : None
        description : Imprime la liste des livres disponibles.
    """
    def afficherLivreDispo(self):
        for livre in self._livres:
            if livre.getDispo() == True:
                print(livre)

    """
        Argument : Aucun
        retour : None
        description : Imprime une liste de livre par genre.
    """
    def afficherLivreGenre(self):
        listGenre = []
        for livre in self._livres:
            listGenre.append(livre.getGenre())
        set_listGenre = set(listGenre)
        new_listGenre = list(set_listGenre)

        for genre in new_listGenre:
            print(genre, ":\n")
            for livre in self._livres:
                if livre.getGenre() == genre:
                    print(livre)

    """
        Argument : Aucun
        retour : None
        description : Imprime une liste de livre par auteur.
    """
    def afficherLivreAuteur(self):
        listAuteur = []
        for livre in self._livres:
            listAuteur.append(livre.getAuteur())
        set_listAuteur = set(listAuteur)
        new_listAuteur = list(set_listAuteur)

        for auteur in new_listAuteur:
            print(auteur, ":\n")
            for livre in self._livres:
                if livre.getAuteur() == auteur:
                    print(livre)

    """
        Argument : Aucun
        retour : None
        description : Imprime une liste de livre par catégorie.
    """
    def afficherLivreCategorie(self):
        listCategorie = []
        for livre in self._livres:
            listCategorie.append(livre.getCategorie())
        set_listCategorie = set(listCategorie)
        new_listCategorie = list(set_listCategorie)

        for categorie in new_listCategorie:
            print(categorie, ":\n")
            for livre in self._livres:
                if livre.getCategorie() == categorie:
                    print(livre)

    """
        Argument : Aucun
        retour : None
        description : Imprime une liste de livre par langue.
    """
    def afficherLivreLangue(self):
        listLangue = []
        for livre in self._livres:
            listLangue.append(livre.getLangue())
        set_listLangue = set(listLangue)
        new_listLangue = list(set_listLangue)

        for langue in new_listLangue:
            print(langue, ":\n")
            for livre in self._livres:
                if livre.getLangue() == langue:
                    print(livre)

    """
        Argument : la_recherche, string
        retour : resultats, list<livre>
        description : Retourne une liste de livre contenant la recherche dans une de ses infos
    """
    def rechercher(self, la_recherche):
        liste_de_livre = self.getListeLivre()
        resultats = []
        for i in liste_de_livre:
            donnee = i.donneeImportante()
            if donnee.find(la_recherche) != -1:
                resultats.append(i)
        return resultats

    """
        Argument : auteur_name, string
        retour : list<livre>
        description : Obtenir une liste de livre correspondant à l'auteur donné.
    """
    def rechercherAuteur(self, auteur_name):
        resultat = []
        for i in self._livres:
            if i.getAuteur().upper() == auteur_name.upper():
                resultat.append(i)
        return resultat

    """
        Argument : genre_name, string
        retour : list<livre>
        description : Obtenir une liste de livre correspondant à le genre donné.
    """
    def rechercherGenre(self, genre_name):
        resultat = []
        for i in self._livres:
            if i.getGenre().upper() == genre_name.upper():
                resultat.append(i)
        return resultat

    """
        Argument : language_name, string
        retour : list<livre>
        description : Obtenir une liste de livre correspondant à le language donné.
    """
    def rechercherLangue(self, language_name):
        resultat = []
        for i in self._livres:
            if i.getLangue().upper() == language_name.upper():
                resultat.append(i)
        return resultat

    """
        Argument : cat_name, string
        retour : list<livre>
        description : Obtenir une liste de livre correspondant à la catégorie donné.
    """
    def rechercherCategorie(self, cat_name):
        resultat = []
        for i in self._livres:
            if i.getCategorie().upper() == cat_name.upper():
                resultat.append(i)
        return resultat

    """
        Argument : size, string
        retour : list<livre>
        description : Obtenir une liste de livre correspondant à la taille donnée.
    """
    def rechercherTaille(self, size):
        resultat = []
        for i in self._livres:
            if i.getTaille() == size:
                resultat.append(i)
        return resultat

    """
        Argument : list<Livre>
        retour : None
        description : Initialise la liste de livre avec celle donnée en entrée
    """
    def initialiserLivres(self, list_livres):
        self._livres = list_livres

    """
        Argument : list<>
        retour : None
        description : Initialise la liste d'Auteur avec celle donnée en entrée
    """
    def initialiserAuteurs(self, list_auteurs):
        self._auteurs = list_auteurs

    """
        Argument : list<>
        retour : None
        description : Initialise la liste de rayons avec celle donnée en entrée
    """
    def initialiserRayons(self, list_rayons):
        self._rayons = list_rayons

    """
        Argument : list<Personne>
        retour : None
        description : Initialise la liste de personnes avec celle donnée en entrée
    """
    def initialiserUtilisateurs(self, list_utilisateurs):
        self._utilisateurs = list_utilisateurs

    """
        Argument : un_livre, Livre
        retour : None
        description : Ajoute un Livre à la liste de livres de la bibliothèque
    """
    def ajouterLivre(self, un_livre):
        self._livres.append(un_livre)
        if not un_livre.getAuteur() in self._auteurs:
            self._auteurs.append(un_livre.getAuteur())

    """
        Argument : la_personne, Personne
        retour : None
        description : ajoute la_personne à la liste des inscrits
    """
    def inscrirePersonne(self, la_personne):
        self._utilisateurs.append(la_personne)

    """
        Argument : la_personne, Personne
        retour : None
        description : enlève la_personne de la liste des inscrits
    """
    def supprimerPersonne(self, la_personne):
        self._utilisateurs.remove(la_personne)

    def __repr__(self):
        print(f'Nom de Bibliothèque : {self._nom}\n')
        resultat = f'Rayon: {self._rayons}\nAuteurs: {self._auteurs}\nLivres: {self._livres}\nUtilisateurs: {self._utilisateurs}\n'
        return resultat

    def getListeLivre(self):
        return self._livres

    def getNom(self):
        return self._nom

    def getRayon(self):
        return self._rayons

    def getAuteur(self):
        return self._auteurs

    def getUtilisateur(self):
        return self._utilisateurs
