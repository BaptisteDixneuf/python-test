import random
import os

def aleatoire():
    tirage =  random.randint(0,100)
    return tirage

def create_file():
    fichier = open('sauvegarde.txt','w+')
    fichier.write("0\n")
    fichier.close

def save_lines(nb_de_ligne):
    fichier = open('sauvegarde.txt','r+')
    last_line = fichier.readlines()[-1]
    print("la dernière ligne", last_line)
    last_line_number = int(last_line)
    new_line = last_line_number + nb_de_ligne
    fichier.write(f"{new_line}\n")
    print(new_line)
    fichier.close


tirage = aleatoire()
if not os.path.isfile('sauvegarde.txt'):
    create_file()
print(tirage)
save_lines(tirage)




