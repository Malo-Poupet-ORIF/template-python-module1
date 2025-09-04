# Orif section informatique
#
# Exercice 4.6
# Je suis aléatoire 6
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
from random import random
a=True
inte=0
while a==True:
    k=round(random() * 100)
    j=round(random() * 100)
    nm = k if j==k else None
    inte = inte+1
    if nm is not None:
        a=False
print(nm)
print(inte)