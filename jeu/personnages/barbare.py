from personnages.personnage import Personnage
from equipement.armes import Arme
from equipement.armures import Armure

class Barbare(Personnage):

    def __init__(self, 
        pv :int,
        nom : str,
        arme: Arme,
        armure: Armure) -> None:
        
        self.pv = pv
        self.nom = nom
        self.arme = arme
        self.armure = armure

    def attaque(self, perso2 : Personnage):
        Personnage.attaque(self,perso2)
        Personnage.attaque(self,perso2)