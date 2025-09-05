# Ceci est un commentaire complètement aléatoire
from random import randint
nom = {
    "Prénom": "Malo",
    "Nom milieu": "Jean",
    "Nom": "Poupet"
} # Dict, peut être utilisé avec nom["Nom du dict (Ex. "Nom milieu")"] ou nom.get("Nom du dict (Ex. "Nom milieu")")
nomstr = "Malo" # Variable de type string
age = 15 # Int, représente un nombre / chiffre
ageprecis = 15.8 # Float, représente un nombre / chiffre avec une décimale
print(nom["Nom milieu"])
print(f"{nom["Prénom"]} a {age} ans ou plus précisément, {ageprecis} ans.") # Les mettre ici les convertira en str automatiquement de toute façon, on peut aussi convertir avec par exemple str(nom de variable), de meme si un str ne contient que des chiffres tu peux faire int(nom de variable en str)
# Preuve:
print(f"Type: {type(age)}")
agestr = f"{age}"
print(f"Converti en str: {type(agestr)}")
agereconverti = int(agestr) # Remettre en int
print(f"Reconverti en int: {type(agereconverti)}")
# Je suis complétement nul en math mais je vais essayer
# Ici, on peur faire un prix aléatoire entre un certain nombre
max = 100
min = 1
prix = randint(min, max) # On passe les paramètres min et max
# On doit le passer dans l'ordre, sinon il va pas le mettre correctement
# Exemple: Si on fait randint(max, min) il va croire que max c'est le min et min c'est le max
# Si on veut vraiment ne pas passer dans l'ordre, on doit préciser lequel est quoi
# Dans ce cas, dans la librarie "random", la variable a est min et b est max
# Donc on passe randint(a=, b=) ou randint(b=, a=) et ça le passera correctement
print(prix)
# Si on veux choisir le prix, faut attendre que l'utilisateur tape le prix, on peut le faire avec la fonction suivante:
prixChoisi = input("Entrez le prix custom: ")
prixChoisi = int(prixChoisi)
print(prixChoisi)
# On peut appliquer un rabais de 10% en faisant une multiplication:
print(f"Prix avec rabais: {prixChoisi * (1 - 0.10)}")
# On peut aussi additionner les textes
# Exemple:
text1 = "Je "
text2 = "suis "
text3 = "Malo!"
print(text1 + text2 + text3)
# Bizzarement, on peut mettre une fonction dans un dict... ou plus ou moins n'importe quoi
dictAvecFunc = {
    "lafunc": randint
}
print(dictAvecFunc)
print(dictAvecFunc["lafunc"](1, 100))
# Je te parie on peut mettre une func dans une liste
print("func dans list")
afsd = ["hello", randint]
print(afsd[1](1, 100))
# Voila cque je disais, ça marche