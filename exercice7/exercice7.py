saisie = True
liste = []
while saisie:
    my_input = input("\nEntrez un nombre\n")
    if my_input == "q":
        saisie = False
    else:
        nombre = int(my_input)
        liste.append(nombre)



res = []
for i in liste:
    if i not in res:
        res.append(i)

#suppression doublon
print("Ma liste dans doublon : ", res)

print("Max", max(res))
print("Min", min(res))

print("Ma liste trié" , sorted(res))
print("Ma liste trié inversé" , sorted(res, reverse=True))

