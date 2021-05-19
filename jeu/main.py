from personnages.personnage import Personnage
from equipement.armes import Arme
from equipement.armures import Armure

if __name__ == "__main__":
    epee = Arme("Epée simple", 8)
    bouclier = Armure("Bouclier", 800)

    hache_ferme = Arme("Hache de ferme", 15)   
    casque = Armure("Casque", 800)
    
    p1 = Personnage(100,"Lancelot", epee, bouclier)
    p2 = Personnage(100,"Roi Burgonde ", hache_ferme, casque)

    p1.attaque(p2)
    print("Résultats: ")
    print(p1.nom, p1.pv, "PV")
    print(p2.nom, p2.pv, "PV")
    input("=================")

    p2.attaque(p1)
    print("Résultats: ")
    print(p1.nom, p1.pv, "PV")
    print(p2.nom, p2.pv, "PV")
    input("=================")
