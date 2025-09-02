# Orif section informatique
#
# Exercice 1.9
# Calcul de salaire
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
salaire = int(input("Quel est votre salaire brut : "))
salaire = salaire * (1 - 0.042)
#print(f"ton salaire a été réduit a {salaire}")
#print(f"t'as cru que c'était tout bon hein? ha non")
salaire = salaire * (1 - 0.07)
#print(f"maintenant {salaire}")
#print(f"c'est pas tout")
salaire = salaire * (1 - 0.025)
#print(f"encore réduit: {salaire}")
#print(f"on te vole ma foi")
salaire = salaire * (1 - 0.01)
#print(f"ptet tu as encore réduit: {salaire}")
salaire = salaire * (1 - 0.013)
#print(f"hehehe: {salaire}")
salaire = salaire * (1 - 0.013)
salaire = salaire * (1 - 0.07)
#print(f"j'avait dit que c'etait ce que t'avais? non, ce qui est la c'est ce que tu as en dette {salaire}")
#print(f"va travailler")
import time
print(f"tu as {salaire}...")
time.sleep(5)
print("en dette, tu croyais que t'était tout bon hein? non, mange les restes de ton frigo")