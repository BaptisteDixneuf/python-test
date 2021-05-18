n = input("Quelle table voulez vous afficher ?\n")
nombre = int(n)

liste : list[str] = []
for i in range (1,21) : 
    calcul = i*nombre
    if(calcul % 3 == 0):
        chaine = "{}* ".format(calcul)
        liste.append(chaine)
    else:
        chaine = str(calcul)        
        liste.append(chaine)
    
print(liste)

ma_chaine = " ".join(liste)
print(ma_chaine)
