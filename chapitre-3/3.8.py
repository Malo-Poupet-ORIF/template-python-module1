from random import randint
print("Devinez un nombre entre 1 et 100")
max = 100
min = 1
i = randint(min, max)
for s in range(0, 10):
    d = int(input(f"Tentative {s} : "))
    if d == i:
        print("Gagné!")
        break
    elif d < i:
        min = d if d > min else min
        print(f"Le nombre mystérieux se situe entre {min} et {max}")
    elif d > i:
        max = d if d < max else max
        print(f"Le nombre mystérieux se situe entre {min} et {max}")