class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = 0
        self.nopeus = 0

    def kiihdytä(self, nopeus_muutos):
        if (self.nopeus + nopeus_muutos) > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif (self.nopeus + nopeus_muutos) < 0:
            self.nopeus = 0
        else:
            self.nopeus += nopeus_muutos
        print(self.nopeus)

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += (self.nopeus * tuntimäärä)
        self.tulosta_tiedot()

class Sähköauto(Auto):
    #rekkari, huippis, akkukapasiteetti
    def __init__(self, rekisteritunnus, huippunopeus, akunkapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akunkapasiteetti = akunkapasiteetti
    def tulosta_tiedot(self):
        print(f"Sähköauto kulki {self.kuljettu_matka} km")

class Polttomoottoriauto(Auto):
    #rekkari, huippis, tankinkoko
    def __init__(self, rekisteritunnus, huippunopeus, tankinkoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankinkoko = tankinkoko
    def tulosta_tiedot(self):
        print(f"Polttomoottoriauto kulki {self.kuljettu_matka} km")

#Pääohjelma missä luodaan 1 sähkis ja 1 polttis
auto1 = Sähköauto("GGI-123", 160, 80)
auto2 = Polttomoottoriauto("WPI-321", 148, 55)

#Autot ajaa 3h ja tulostaa matkamittarilukeman.
auto1.kiihdytä(90)
auto1.kulje(3)
auto2.kiihdytä(85)
auto2.kulje(3)

