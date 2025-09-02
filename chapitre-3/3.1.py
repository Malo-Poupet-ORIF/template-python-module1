g = int(input("indiquez le nombre : "))
try:
    if g < 50:
        print("Inférieur a 50")
    elif g > 50:
        print("Supérieur a 50")
    elif g == 50:
        print("égal a 50")
except Exception as e:
    print(f"Mais tu fais quoi??? {e}")