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


class CompteEpargne(CompteBancaire):
    
    def __init__(self, nom : str = 'Dupont', solde : float = 1000, taux_interet = 0.03):
        CompteBancaire.__init__(self, nom, solde)
        self.taux_interet =  taux_interet  
   

    def changeTaux(self,taux_interet):
        self.taux_interet = taux_interet
    
    def capitalisation(self, nombre_mois):
        print("Taux", self.taux_interet, "solde", self.solde)
        calcul = self.solde
        for i in range(nombre_mois):
            calcul = calcul + calcul * self.taux_interet
        
        print(calcul)



compte1 = CompteEpargne()
compte1.capitalisation(1)
compte1.capitalisation(2)
