class Armure:

    def __init__(self, nom : str, point_defense : int) -> None:
        self.nom = nom
        self.point_defense = point_defense

    def __str__(self) -> str:
        ma_chaine = "Armures, nom : {} , point de défense : {} ".format(self.nom, self.point_defense)
        return ma_chaine
    