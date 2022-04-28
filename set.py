"""**********************************LES ENSEMBLES**********************************"""
print("\r")
"""
Les ensembles (set) font partis des 4 types de données intégré à python qui vont nous permettre de stocker une collection de 
donnée dans un variable.C'est une collection non ordonnée , non indexable et qui n'autorise pas les doublons . toutfois d'un 
ensemble est crée nous ne pouvons pas modifier ces elements mais nous pouvons supprimer et add de nouveaux elements .
A cela s'ajoute le fait que les valaurs en doubles seront ignorées
"""

"""CREATION D'UN ENSEMBLE"""
legume={"chou","tomate","brocoli","courgette","chou","concombre"}
print(legume)

"""Voir le nombre d'element dans l'ensemble"""
print(len(legume))

#le constructeur set() nous permettra de créer un ensemble et même souvent de convertir un autre type de donnée integré en ensemble
fruit=("mangue","cerise","raisin","raisin","pomme","fraise","mange","kiwi")
fruits=set(fruit)    #convertir le tuple en ensemble
print(fruits)

# Parcourir l'ensemble
for i in legume:
    print(i,end=" ")
print("\r")

#Verifier la presence d'un element dans la listre
print("mangue" in fruits) #retourne True or False

#Ajouter un item
legume.add("aubergine")
print(legume)

#Joindre des ensembles
legume.update(fruits)
print(legume)

#mettre les element d'une liste dans l'ensemble
frt=("grenade","framboise","avocat")
fruits.update(frt)
print(fruits)

"""FUSION DE DEUX ENSEMBLES"""

#1 union methode
print("Fusionner avec union".center(155,"_"))
fusion=legume.union(fruits)     #exclus les element en double
print(fusion)

#2 update methode
print("Fusionner avec update méthode".center(155,"_"))
legume.update(fruits)          #exclus les element en double
print(fruits)

#3 Garder les elements qui se repete dans les deux ensembles
print("Garder uniquement que les doublons".center(155,"_"))
fusion.intersection_update(fruits)
print(fusion)

#4 Ne pas concerver les doublons
print("Ne pas concerver les doublons".center(155,"_"))
legume.symmetric_difference_update(fruits)
print(legume)

"""Supprimer un element de l'ensemble"""

#1 Supprimer avec .remove()
print("Supprimer avec la remove méthode".center(155,"_"))
fruits.remove("framboise")
print(fruits)

#2 Supprimer avec .discard
print("Supprimer avec la discard méthode".center(155,"_"))
fruits.discard("fraise")      #L'avantage d'ituliser discard est que si la valeur que vous desirez supprimer n'existe pas il y aura pas d'erreur
print(fruits)

#3 Supprimer avec .pop()
print("Supprimer avec la pop méthode".center(155,"_"))
frt=fruits.pop()
print(f"la valeur supprimée est {frt}".center(155))
print(fruits)

#4 Vider l'ensemble avec la clear méthode
print("Vider l'ensemble avec la clear méthode".center(155,"_"))
legume.clear()
print(legume)

#5 Supprimer completement l'ensemble
print("Supprimer completement l'ensemble avec le mot clé del".center(155,"_"))
del fruits



print("\r")