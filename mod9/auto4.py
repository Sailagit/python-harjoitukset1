# uuden auton kuljettu matka on automaattisesti nolla
# Pääohjelma lista, joka koostuu 10 toistolla luodusta auto-oliosta
# auton huippunopeus arvotaan 100-200 väliltä
# rekisteritunnus abc-1, abc-2 jne.

import random

class Auto:
    def __init__(self, huippunopeus, rekisteritunnus):
        self.huippunopeus = huippunopeus
        self.rekisteritunnus = rekisteritunnus
        self.kuljettu_matka = 0
        self.nopeus = 0

    def __str__(self):
         return f"[{self.rekisteritunnus}] {self.kuljettu_matka}km (V max.{self.huippunopeus}km/h. V {self.nopeus}km/h)"
    
    def kiihdytä(self, nopeus_muutos):
        if (self.nopeus + nopeus_muutos) > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif (self.nopeus + nopeus_muutos) < 0:
            self.nopeus = 0
        else:
            self.nopeus += nopeus_muutos
    
    def kulje(self, tuntimäärä):
        self.kuljettu_matka += (self.nopeus * tuntimäärä)

kilpa_autot = []
for i in range(1, 11):
    uusi_auto = Auto(random.randint(100, 200), f"ABC-{+ i}" )
    kilpa_autot.append(uusi_auto)

kilpailu_voitettu = False
while not kilpailu_voitettu:
    for auto in kilpa_autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
             kilpailu_voitettu = True
             break

kilpa_autot.sort(key = lambda auto: auto.kuljettu_matka, reverse = True)

for auto in kilpa_autot:
     print(str(auto))    

