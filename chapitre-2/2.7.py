# Orif section informatique
#
# Exercice 2.7
# Compte en arrière chaque seconde et BOOM a la fin
#
# Auteur : Malo Poupet
# Date   : 02.09.2025
import time
# import winsound Non-disponible dans cet env
for b in range(20, 0, -1):
    print(b)
    time.sleep(1)
    if b <= 1:
        print("BOOM!")
    #    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)