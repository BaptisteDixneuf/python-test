n = input("Quelle table voulez vous afficher ?\n")
nombre = int(n)

for i in range(1, nombre): 
    for j in range (nombre, 1, -1):
        #print (i , j)
        if(i+j == 8):
            print("(", i , ", " , j ,")")