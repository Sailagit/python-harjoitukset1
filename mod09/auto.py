# luokka auto ominaisuudet ovat rekisteritunnus, huippunopeus, tämän hetkinen nopeus ja kuljettu matka.
class Auto:
    def _init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.atm_nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", "142km/h")

print(F"{auto.rekisteritunnus} huippunopeus on {auto.huippunopeus}, tämän hetkinen nopeus on {auto.atm_nopeus} ja kuljettu matka on {auto.kuljettu_matka}.")