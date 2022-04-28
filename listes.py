"""********************listes en python********************"""


"""declaration d'une liste vide"""
list1=[]

"""liste avec des elements"""
liste2=["clavier","souris","webcam","disque-dur"]

"""la longueur de notre liste"""
print(len(liste2))

"""accedé à un element de liste"""
print(liste2[1])

"""accedé à une plage d'item"""
print(liste2[1:4])

"""modifier"""

##1 un item
liste2[2]="mouse"
print(liste2)

##2 une plage
liste2[1:3]=["souris","webcam"]
print(liste2)

"""insert"""

#Inserer à la position de notre choix
list1.insert(0,"ecran")
print(list1)

#inserer en fin de liste
list1.append("clé-USB")
print(list1)

"""fusion"""

#fusionner deux listes
list1.extend(liste2)
print(list1)

"""supprimer"""

#1 Supprimer avec la methode remove(valeur)
list1.remove("webcam")
print(list1)

#2 Supprimer avec pop() methode en renseignant l'index
list1.pop(2)
print(list1)
#Nb: si nous ne renseignons pas l'index le dernier element de la liste sera supprimé


#3 Supprimer avec del
del list1[1]
print(list1)
#Nb: si nous ne renseignons pas l'index la liste sera supprimé

#voir la position d'un item dans la liste
index=list1.index("ecran")
print(f"clavier est à l'index {index} c'est-à dire l'element {index+1} de la liste")

#voir le nombre de fois qu'une valeur apparait dans la liste : .count()
nombre=list1.count("ecran")
print(f"Ecran est {nombre} fois dans la liste")

#trier par ordre alphabetique evec la méthode .sort()
print("Liste suivant l'ordre alphabetique".center(150,"-"))
list1.sort()
print(list1)

#4 supprimer avec clear()
liste2.clear() #vide la liste
print(liste2)

"""Afficher les elements d'une liste à l'aide de boucle"""

#afficher le contenu à l'aide de la boucle for
##Méthode 1
print("Avec la boucle for :", end=" ")
for i in list1:
    print(i, end=" ")
print("\r")

##Méthode2
for a in range(0,len(list1)):
    print(list1[a],end=" ")
print("\r")

#afficher le contenu à l'aide de la boucle while
print("Avec la boucle while :", end=" ")
compt=0
while compt<len(list1):
    print(list1[compt], end=" ")
    compt+=1 # important pour ne pas être face a une boucle infinie
print("\r")
print("******LE RESULTAT EST LE MEME******")



