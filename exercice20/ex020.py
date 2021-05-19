from __future__ import annotations

class CompteBancaire():

    def __init__(self, nom : str = 'Dupont', solde : float = 1000):
       self.nom = nom
       self.solde = solde

    def depot(self, montant: float):
        self.solde = self.solde + montant

    def retrait(self, montant: float):
        self.solde = self.solde - montant

    def afficher(self):
        ma_chaine = "nom : {} , solde : {} ".format(self.nom, self.solde)
        print(ma_chaine)

    def __str__(self):
        ma_chaine = "nom : {} , solde : {} ".format(self.nom, self.solde)
        return ma_chaine

    def __lt__(self, other: CompteBancaire):
        if self.solde < other.solde
        return True

compte1 = CompteBancaire()
compte1.depot(50)
compte1.afficher()
compte1.retrait(50)
compte1.afficher()


compte2 = CompteBancaire("DIXNEUF")
compte2.depot(50)
compte2.afficher()
compte2.retrait(50)
compte2.afficher()

compte1.retrait(20)
compte2.retrait(19)

compte1.afficher()
compte2.afficher()

print("-----")
compte1 = compte2
compte1.afficher()
compte2.afficher()
compte2.retrait(10)
compte1.afficher()
compte2.afficher()

compte1.retrait(10)
compte1.afficher()
compte2.afficher()


print(compte1)




