import traceback


note = 0 
listeNote = []
listeCoefficient = []
while note >= 0 : 
    try:
        inputUser = input("Entrez un nombre positif et son coefficient ou négatif pour quitter: \n" )
        listeSplit = inputUser.split(" ")
        note = float(listeSplit[0])
        coefficient = float(listeSplit[1])
        print("note : ", note, ", coefficient" , coefficient)
    except ValueError as error:
        print("ceci n'est pas un nombre")       
        #traceback.print_exception(type(error), error, error.__traceback__)
        #traceback.print_tb(error.__traceback__)
    except IndexError as error:
        print("Ceci n'est pas un nombre")
    else :        
        if note >= 0:
            listeNote.append(note)
            if coefficient != None:
              listeCoefficient.append(coefficient)
            else :
                listeCoefficient.append(0)     


print("les notes sont :" , listeNote)
print("les coefficients sont :" , listeNote)
print("il y ", len(listeNote))

if len(listeNote) > 0:

    calcul = 0
    for index, valeur in enumerate(listeNote):
        calcul = calcul + valeur*(listeCoefficient[index])

    moyenne = calcul/sum(listeCoefficient)
    print("Moyenne" , moyenne)
else: 
    print("Vous n'avez rentré aucune note")


