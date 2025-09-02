# Orif section informatique
#
# Exercice 1.10
# Calcul de prix
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
truc1 = int(input("Longeur (m) : "))
truc2 = int(input("Largeur (m) : "))
truc3 = int(input("Profondeur (m) : "))
prix = float(input("Prix 1m: "))
print(f"Surface : {truc1 * truc2 * truc3}m")
print(f"Prix : {truc1 * truc2 * truc3 * prix}CHF")