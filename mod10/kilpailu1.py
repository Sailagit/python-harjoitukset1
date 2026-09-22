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

class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, kilpa_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.kilpa_autot = kilpa_autot

    def tunti_kuluu():
        for auto in kilpa_autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne():
        kilpa_autot.sort(key = lambda auto: auto.kuljettu_matka, reverse = True)
        for auto in kilpa_autot:
            print(str(auto))

    def kilpailu_ohi():
        while not kilpailu_voitettu:
                if auto.kuljettu_matka >= 8000:
                    kilpailu_voitettu = True
                    return True
                else:
                    return False
kilpa_autot = []
for i in range(1, 11):
    uusi_auto = Auto(random.randint(100, 200), f"ABC-{+ i}" )
    kilpa_autot.append(uusi_auto)

kisa = Kilpailu("Suuri romuralli", 8000, kilpa_autot)

while not kisa.kilpailu_ohi():
    kisa.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kisa.tulosta_tilanne()