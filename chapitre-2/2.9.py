# Orif section informatique
#
# Exercice 2.9
# Livret scolaire
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
print("""Orif section informatique - Exercice 2.9 - Malo Poupet
--- Programme d’aide à la répétition du livret ----
---------------------------------------------------""")
d = int(input("Quel livret voulez-vous ?"))
e = int(input("A combien voulez-vous qu’il stoppe ?"))
for i in range(1, e+1):
    print(f"{i} * {d} = {i * d}")