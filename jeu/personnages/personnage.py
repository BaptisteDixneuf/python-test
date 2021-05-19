from __future__ import annotations
from equipement.armes import Arme
from equipement.armures import Armure

class Personnage:

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
        perso2.pv = perso2.pv - self.arme.point_attaque


    def recoit_attaque(self, arme : Arme):
        self.pv = self.pv - arme.point_attaque
