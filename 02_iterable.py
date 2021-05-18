a = "Je code"
for element in a:
 	print(element)


villes=["Paris","Lyon","Marseille","Toulouse"]
for element in villes:
 	print(element)

print(villes[0])


ma_liste = []           # On déclare une liste vide

type(ma_liste )         # retourne le type d’une liste : “list”

ma_liste.append("a")    # ajoute la lettre ‘a’ dans la liste

ma_liste.insert(0,"f")  # ajoute la lettre ‘f’ dans la liste en position 0

print(ma_liste)         # On affiche la liste (qui ne contient que les lettres ‘a’ et ‘f’)

print(ma_liste[0])      # On affiche le premier élément de la liste (ici ‘a’)

ma_liste.count

liste: list[str] = []

len(liste)