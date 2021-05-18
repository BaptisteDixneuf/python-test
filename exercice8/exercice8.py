noms = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
grand_noms = []
petit_noms = []

for nom in noms:
    if len(nom) <6:
        petit_noms.append(nom)
    else:
        grand_noms.append(nom)

print("La liste des grands prénoms est", grand_noms)
print("La liste des petits prénoms est", petit_noms)

chaine_grand = ", ".join(grand_noms)
chaine_petit = ", ".join(petit_noms)

print("La liste des grands prénoms est", chaine_grand)
print("La liste des petits prénoms est", chaine_petit)