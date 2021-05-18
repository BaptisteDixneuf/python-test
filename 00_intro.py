from typing import AsyncGenerator


print("Hello Baptiste") # Exemple de commentaire

#addition
addition = 2+2

#soustraction
soustraction = 2-1

print(addition)
print(soustraction)


b= 5
print(type(b))

c: bool = 3
print(type(c))

chaine = "ici mon text d'aujourd'hui"

chaine2 = 'ici mon text d\'aujourd\'hui'

age = 30
nom = "Bob"
# chainecon_concatene = "Je suis " + nom + "et j'ai :" + age # a éviter
chaine_concatene = f"Je suis {nom} et j'ai {age}"
print (chaine_concatene)


chaine_concatene = "Je suis {} et j'ai {}".format(nom,age)
print (chaine_concatene)

nombre = 5
print(str(nombre))
print(float(nombre))

chaine = "TEST"
# int(chaine) => pas possible, attention a cast


decimal = 5.5
print(int(decimal)) # attention ne fonctionne pas toujours


print("Bonjour", decimal, int(decimal), "test", sep=" - ", end="\t")



my_input = input("\nSaisisez quelque chose ?\n")
print (my_input)
print (type(my_input))


