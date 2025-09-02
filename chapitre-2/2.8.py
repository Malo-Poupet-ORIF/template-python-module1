import time
# import winsound Non-disponible dans cet env
for b in range(20, 0, -1):
    print(b)
    time.sleep(1)
    if b <= 10:
        print(f"Plus que {b} secondes avant explosion.")
        if b <= 1:
            print("BOOM!")
            #winsound.PlaySound("sound.wav", winsound.SND_FILENAME)