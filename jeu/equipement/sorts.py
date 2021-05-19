class Sort():

    def __init__(self, nom : str, point_attaque : int, mana : int) -> None:
        self.nom = nom
        self.point_attaque = point_attaque
        self.mana = mana
    

    def __str__(self) -> str:
        ma_chaine = "Sort, nom : {} , point d'attaque : {} , mana ; {} ".format(self.nom, self.point_attaque, self.mana)
        return ma_chaine