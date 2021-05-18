def factorielle(n):
    """
    calcul la factorielle d’un nombre. 
    """
    return 1 if n == 0 else n * factorielle(n-1)

print(factorielle(0))
print(factorielle(1))
print(factorielle(5))


def element_max(liste, debut= 0, fin=-1):   
    max = 0
    for element in liste[debut:fin] :
        if(element >  max ):
            max = element
    return max

def element_max2(liste, debut= 0, fin=-1):   
   return max(liste[debut:fin])
       
   

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(element_max(serie))
print(element_max(serie,2,5))
print(element_max(serie,2))
print(element_max(serie,fin=3, debut=1))

print(element_max2(serie))
print(element_max2(serie,2,5))
print(element_max2(serie,2))
print(element_max2(serie,fin=3, debut=1))