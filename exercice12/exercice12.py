import traceback


nombre = 0 
liste = []
while nombre >= 0 : 
    try:
        n = input("Entrez un nombre positif ou négatif pour quitter: \n" )
        nombre = float(n)
    except ValueError as error:
        print("ceci n'est pas un nombre")       
        traceback.print_exception(type(error), error, error.__traceback__)
        traceback.print_tb(error.__traceback__)
    else :
        if(nombre >= 0):
            liste.append(nombre)

print("les notes sont :" , liste)
print("il y ", len(liste))
if len(liste) > 0:
    print("La moyenne de ce ces notes est ", sum(liste)/ len(liste))
else: 
    print("Vous n'avez rentré aucune note")


