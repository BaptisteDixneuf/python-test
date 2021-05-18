from decimal import Decimal
my_input = input("\nEntrez votre vitesse en km/h ?\n")
kilometre_heure = float(my_input)
mile = 1.609
calcul  = kilometre_heure / mile
print (kilometre_heure, 'Km/h = ', calcul.__round__(2), 'm/h')

ma_chaine = "{:.2f} km/h = {:.2f} m/h".format(kilometre_heure, calcul)

print(ma_chaine)