"""*******************************************************TUPLES*******************************************************"""
"""Création de tuple"""

"""
les tupes font partir des 4 types de donnée integrés à python, les 3 autres sont list,set,dictionnaire.
ce sont des collections ordonnées
Avec les tuple nous pouvons mettre plusieurs valeur en une seule variable .Cependant cette variable  accepte les doublons sera immuable et- autorise les valeurs en double .
Pour sa declaration on utilise les parenthèses , exemple: tuple=() 
"""
print("\r")

"""Créons un tuple fruit qui va contenir certain fruits"""
fruit=("mangue","cerise","raisin","raisin","pomme","fraise","mange","kiwi")
print(fruit) #imprimer le tuple
print("\r")

"""Créer un tuple avec un seul element """
legume=("ail",) #si ne mettez pas la virgule , python ne reconnaitrera pas legume comme une liste
print(legume)
print("\r")

"""longueur d'une tuple"""
print(len(fruit))
print("\r")

"""Acceder a une valeur precise dans notre tuple(fruit)"""
#Et oui ça marche comme pour les listes puise qu'ils sont tous le deux des collections ordonnées
print(fruit[1])#nous imprimons le cerise
print("\r")

"""indexage negative pour dire que sa commence à la fin"""
print(fruit[-5])#imprime raisin
print("\r")

"""Gamme d'index"""

#Nous allons spécifier notre plage d'index en indiquant le debut et la fin
print(fruit[2:5]) #la valeur à l'index 2 est inclus parcontre celle à l'index 5 est exclus
print("\r")

"""Verifier l'existence d'une valeur dans un tuple"""
if "mangue" in fruit:
    print("cette valeur existe déjà dans la tuple")
else:
    print("Cette valeur n'exixte pas dans la tuple")
#dans notre cas la machine va afficher le premier message car le tuple contient mangue
print("\r")

"""
Depuis le debut vous êtes informé que les tuples sont immuables .
Ainsi il est impossible pour les programmeur de modifier , supprimer et ajouter un element.Cependant il existe des moyens
pour contourner cette restruction
"""
print("\n")

#1 MODIFIER: pour modifier le tuple
print(f"Modifier {fruit[1]} en citron".center(155,"_"))
liste=list(fruit) #convertir le tuple en liste
liste[1]="citron" #modifier la liste
fruit=tuple(liste) #convertir la liste en tuple
print(fruit)
print("\n")

#2 Ajourter une valeur à notre tuple
print("Ajouter la valeur cerise a sa place et mettre grenade a la fin".center(155,"_"))
liste=list(fruit)        #convertir le tuple en liste
liste.insert(1,"cerise") #remettre cerise à l'index 1
liste.append("grenade")  #mettre grenade
fruit=tuple(liste)       #convertir la liste en tuple
print(fruit)
print("\r")

"""JOINDRE DES TUPLES"""

#1 Ajouter un tuple à un tuple tuple"""
print("Ajouter un tuple à un tuple".center(155,"_"))
fruit2=("ananas","avocat","framboise","orange","papaye") #Créatioon d'un tuple
fruit+=fruit2                                            #ajout de fruit2 à fruit
print(fruit)
print("\n")

#3 supprimer une valeur d'un tuple
print("Supprimer un element".center(155,"_"))
sup=list(fruit2)
sup.remove("papaye") #supprimer papaye
fruit2=tuple(sup)
print(fruit2)
print("\r")

#deballer un tuple
##1
(a,b,c,d,e)=fruit2
print(f"{a},{b},{c},{d},{e}")

##2 si le nombre de variable est inferieure au nombre de valeur ,mettre le reste des valeurs dans une variable liste
(var1,*var2)=fruit

"""Parcourir la tuple avec une boucle"""

#la boucle for
print("Les element de la tuple avec la boucle for".center(155,"_"))
for i in fruit:
    print(i,end=" ")
print("\n")

#avec la boucle while
print("Les element de la tuple avec la boucle while".center(155,"_"))
genius=0
while genius <len(fruit):
    print(fruit[genius],end=" ")
    genius+=1
print("\n")

"""METHODE SUR LES TUPLES"""

#1 .count() : utiliser cette méthode pour voir le nombre de fois qu'une valeur intervient dans un tuple
nombre=fruit.count("mangue")
print(f"cette valeur intervient {nombre}")

#2 .index() : pour retrouver l'iindex d'un element
ind=fruit.index("mangue")
print(f"Mangue intervient à l'index {ind} ")


