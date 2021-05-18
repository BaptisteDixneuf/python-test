import random

mystere = random.randint(0,1000)


essai = 0
trouve = False
while trouve == False: 
    my_input = input("\nEntrez un nombre\n")
    nombre = int(my_input)
    essai +=1
    if nombre == mystere : 
        print("Bravo, vous avez trouvé")
        print("Bravo, vous avez mis", essai, "essais")
        trouve = True
    elif nombre < mystere:
        print("Le nombre est plus grand")
    elif nombre > mystere:
        print("Le nombre est plus petit")
