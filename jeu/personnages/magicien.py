from personnages.personnage import Personnage
from equipement.armes import Arme
from equipement.armures import Armure
from equipement.sorts import Sort

class Magicien(Personnage):

    def __init__(self, 
        pv :int,
        nom : str,
        arme: Arme,
        armure: Armure,
        sort: Sort) -> None:
        
        self.pv = pv
        self.nom = nom
        self.arme = arme
        self.armure = armure
        self.sort = sort

    def attaque(self, perso2 : Personnage):
       while True :
            try:
                n = input("Choisir 1 => Attaque magique (sort) , 2 => Attaque physique")
                choix = int(n)
            except:
                print("Erreur de valeur")
            else :
                if n == 1:
                    """ 
                    Sort
                    """
                    
                elif n == 1:
                    """
                    attaque
                    """
                    Personnage.attaque(self,perso2)
           