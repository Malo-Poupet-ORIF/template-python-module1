# Orif section informatique
#
# Exercice 3.5
# Question de status
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
ages = {
    7: "groupe Cadets",
    12: "groupe Louveteaux",
    18: "groupe Scout",
    "18+": "chef de meute"
}
i = int(input("Age : "))
if i <7:
    print(ages.get(7))
elif i <12:
    print(ages.get(12))
elif i <18:
    print(ages.get(18))
else:
    print(ages.get("18+"))