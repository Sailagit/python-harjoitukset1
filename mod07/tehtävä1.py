import random

def noppaheitto():
    heitto = random.randint(1,6)
    return heitto

tulos = noppaheitto()

while True:
    tulos = noppaheitto()
    print(tulos)
    if tulos == 6:
        break
