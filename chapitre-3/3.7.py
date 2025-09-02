from random import randint
print("Devinez un nombre entre 1 et 100")
i = randint(1, 100)
for s in range(0, 10):
    d = int(input(f"Tentative {s} : "))
    if d == i:
        print("Gagné!")
        break
    elif d < i:
        print("Trop bas")
    elif d > i:
        print("Trop haut")