for nombre in range (100):
    
    #print( "nombre en cours : " , nombre)
    i = 0
    countdiviseur = 0

    #on cherche les diviseurs
    for i in range (nombre):
        if i != 0 and  i != 1 and  i != nombre:  
            modulo = nombre % i
            if modulo == 0 :                 
                countdiviseur +=1

    if countdiviseur == 0: 
        print(nombre ," est un nombre premier")

