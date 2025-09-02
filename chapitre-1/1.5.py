# Orif section informatique
#
# Exercice 1.5
# Calculer le diamètre + circonférence a partir du rayon
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
from math import pi as p
r = int(input("Rayon : "))
d = r * 2
c = p * 2 * r
print(f"Diamètre : {d}")
print(f"Circonférence : {c}")