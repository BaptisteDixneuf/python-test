def trier_liste(*args):
    liste_pair = []
    liste_impair = []
    print(*args)
    for item in args:
        if item % 2 == 0 : 
            liste_pair.append(item)
        else:
            liste_impair.append(item)
    liste_pair.sort
    liste_impair.sort
    joined_list = liste_pair + liste_impair
    print (joined_list)

trier_liste(2, 1, 8, 3, 4, 6, 9, 7, 5)
#liste = [2, 1, 8, 3, 4, 6, 9, 7, 5]
#trier_liste(liste)