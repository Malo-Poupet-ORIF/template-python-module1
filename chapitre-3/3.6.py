# Orif section informatique
#
# Exercice 3.6
# Grouper
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
m = input("Marque : ").lower()
if m in ["volvo", "ford", "fiat", "opel"]:
    print("general motors")
elif m in ["vw", "audi", "skoda", "seat "]:
    print("VAG")
elif m in ["peugeot", "citroën"]:
    print("PSA")
elif m in ["renault", "nissan"]:
    print("Groupe Renault")