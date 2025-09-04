# Orif section informatique
#
# Exercice 4.5
# Je suis aléatoire 5
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
from random import random
a=True
while a==True:
    k=round(random() * 100)
    j=round(random() * 100)
    nm = k if j==k else None
    if nm is not None:
        a=False
print(nm)