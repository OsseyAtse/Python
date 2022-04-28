"""*************************************DICTIONNAIRE**********************************"""

"""
Les dictionnaires sont des collcteur de donnée utilisé pour stocker des valeurs de donnée dans des pairs clé:valeur.
Ils sont ordeonnées , modifiable et n'autorise pas les valeur en double
"""
print("\n")

#Créer un dictionnaire
dic={"Nom":"ATSE","Prénom":"Ossey","Âge":"19 ans"}
print(dic)

#Afficher une valeur de notre dictionnaire
print(f"Votre vous êtes {dic['Nom']} {dic['Prénom']} âgé de {dic['Âge']}")

#affficher à l'aide de la methode get()
print(dic.get('Prénom'))

#afficher les clés du dictionnaire avec la méthode keys()
x=dic.keys()
print(f"Les clés du dictionnaire sont {x}".center(155))

#afficher la liste des valeurs avec values() méthode
y=dic.values()
print(f"Les valeurs du dictionnaire sont {y}".center(155))

#obtenir une liste de pairs avec items méthode
z=dic.items()
print(z)                      #les pairs sont sous forme de tuple dans une liste

# voir si une clé existe dans notre dictionnaire
if "Nom" in dic:
    print("Cette clé est dans le dictionnaire")
else:
    print("Cette clé n'existe pas dans le dictionnaire")

#nombre d'element dans le dictionnaire
print(len(dic))

#un dictionnaire peu contenir des listes
dict2={"marque":"ford","année":2022,"couleur":["rouge","blanche","verte"]}

"""MODIFIER"""

#1 modifier une valeur dans le dictionnaire
dic["Nom"]="MICKEY"
print(dic)

#2 modifier avec la methode update
dic.update({"Prénom":"SMILE"})
print(dic)

"""AJOUTER UN ELEMENT"""

#1
dic["taille"]="1m79"
print(dic)

#2 avec la méthode update
dic.update({"commune":"cocody"})
print(dic)

"""SUPPRIMER"""

#1 avec pop , ici il faut spécifier la clé
dic.pop('Âge')
print(dic)

#3 avec popitem , qui va supprimer le dernier element
dic.popitem()
print(dic)

#4 avec clear , pour vider le dictionnaire
dict2.clear()
print(dict2)

#5 avec le mot-clé del
del dic["Nom"]
print(dic)
#NB: on peut toute fois utiliser del pour supprimer complement le dictionnaire avec l'instruction : del NomDictionnaire

"""afficher avec une boucle"""

#1 afficher les clés
for x in dic:
    print(x)

#2 afficher les valeurs avec values méthode
for y in dic.values():
    print(y)

"""COPIER UN DICTIONNAIRE"""

#1 avec copy()
NewDict= dic.copy()
print(NewDict)

#2 avec la fonction dict
NewDict2=dict(dic)
print(NewDict2)

"""DICTIONNAIRE IMBRIQUES"""
#1 Un dictionnaire peut contenir plusieurs autre dictionnaire c'est ce qu'on appelle dictionnaire imbriqué
enfants={
    "enfant1":{"nom":"Luis","age":"15 ans","classe":"3ieme","etablissement":"LMCA"},
    "enfant2":{"nom":"Fabien","age":"13 ans","classe":"6ieme","etablissement":"LMCA"},
    "enfant3":{"nom":"Auriel","age":"6 ans","classe":"CP2","etablissement":"GSLPC"}
}

#2 créer deux dictionnaire puis créer un qui contient les deux
papa={"nom":"Guibé","age":"35 ans","fonction":"Medecin","etablissement":"CHU-Cocody"}
maman={"nom":"yolande","age":"34 ans","fonction":"comptable","etablissement":"BNCI"}
parents={"papa":papa,"maman":maman}

print(enfants)
print(parents)
print("\n")