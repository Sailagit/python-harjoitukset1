import random

def noppaheitto(tahkot):
    heitto = random.randint(1, tahkot)
    return heitto

maksimi = int(input("Maksimisilmäluku: "))

while True:
    tulos = noppaheitto(maksimi)
    print(tulos)
    if tulos == maksimi:
        break