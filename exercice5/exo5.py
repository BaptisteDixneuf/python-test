my_input = input("\nEntrez un nombre\n")
nombre = int(my_input)

calcul = 0
countdiviseur = 0
for i in range (nombre):
    if i != 0 and  i != 1 and  i != nombre:  
        modulo = nombre % i
        if modulo == 0 : 
            print(i ," est un diviseur de", nombre)
            countdiviseur +=1

if countdiviseur == 0: 
    print(nombre ," est un nombre premier")


