""""************************************VARIABLES************************************"""

"""

"""
print("\r")

print("Affectation".center(200, "_"))
"""affectation : les chaines de caractères"""
nom="genius"
prenom="ACADEMY"
slogant=" l'univers des competences "
print(nom)
print(prenom)
print(slogant)

#mettre genius en minuscule
print(nom.upper())

#mettre en majuscule
print(prenom.lower())

#effacer les espaces en debut et en fin de string
print(slogant.strip())

#imprimer GENIUS-ACADEMY
print("J'apprend python avec ", end="")
print(nom.upper(),prenom.upper(), sep="-")

x=slogant.center(100,"_")
print(x)
#afficher la longueur de de la string
print(f"{nom} contient {len(nom)} caractères ,{prenom} contient {len(prenom)} caractères et {slogant} contient {len(slogant)} caractères")

"""modifier"""
#modifier la valeur de la variable
nom="GENIUS TV"
print(f"La nouvelle valeur est {nom}")

#modifier un element precis dans la string


"""Entier"""
#affectation
an=2022
print(f"nous somme en {an}")

print("Recuperation de saisie et affichage".center(150, "_"))

"""Ici nous allons recuperer une chaine de caractere """
NomVariable=input("Entrez votre nom s'il vous plaît! ")
print(f"bonjour {NomVariable.upper()}".center(150))
print("\r")
print("recuperer un entier".center(150, "_"))
"""Recuperer un entier entré au clavier"""
an_nais=int(input("Entrez votre année de naissance s'il vous plaît "))
print(f"vous êtes née en {an_nais}".center(150))
print("GENIUS-ACADEMY,l'univers des compétences".center(150))
print("\r")