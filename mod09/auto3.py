class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 2000

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
        print(self.kuljettu_matka)



auto = Auto("ABC-123", 142)
auto.kiihdytä(60)
auto.kulje(1.5)
auto.kulje(3)
auto.kulje(4.5)


print(F"{auto.rekisteritunnus} huippunopeus on {auto.huippunopeus}km/h, tämän hetkinen nopeus on {auto.nopeus}km/h ja kuljettu matka on {auto.kuljettu_matka}.")