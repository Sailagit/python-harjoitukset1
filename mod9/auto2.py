class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeus_muutos):
        if (self.nopeus + nopeus_muutos) > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif (self.nopeus + nopeus_muutos) < 0:
            self.nopeus = 0
        else:
            self.nopeus += nopeus_muutos
        print(self.nopeus)


auto = Auto("ABC-123", 142)
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.kiihdytä(-200)

print(F"{auto.rekisteritunnus} huippunopeus on {auto.huippunopeus}km/h, tämän hetkinen nopeus on {auto.nopeus}km/h ja kuljettu matka on {auto.kuljettu_matka}.")