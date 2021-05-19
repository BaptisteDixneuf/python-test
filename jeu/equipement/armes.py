class Arme:

    def __init__(self, nom : str, point_attaque : int) -> None:
        self.nom = nom
        self.point_attaque = point_attaque
    

    def __str__(self) -> str:
        ma_chaine = "Armes, nom : {} , point d'attaque : {} ".format(self.nom, self.point_attaque)
        return ma_chaine