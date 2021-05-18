a="Ma jeunesse ne fut qu'un tenebreux orage,\
  Traverse ca et la par de brillants soleils ;\
 Le tonnerre et la pluie ont fait un tel ravage,\
 Qu il reste en mon jardin bien peu de fruits vermeils."

mon_dict = {}
for character in a : 
    character = character.lower()
    print(character)
    if mon_dict.get(character) == None :
        mon_dict[character] = 1
    else:
        mon_dict[character] +=1


print("Analyse du texte" , mon_dict)


