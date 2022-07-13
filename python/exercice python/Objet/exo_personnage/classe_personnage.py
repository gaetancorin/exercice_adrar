
from importlib.abc import MetaPathFinder


class Personnage:
    
    def __init__(self, nom, metier):
        self.nom = nom
        self.metier = metier
        self.niveau = 0
        self.hp = 100
        self.force = 30
        self.inventaire = []
        
        
    def LevelUp(self):
        self.niveau = 10
        
    def GagnerObjet():
        if self.niveau == 20:
            