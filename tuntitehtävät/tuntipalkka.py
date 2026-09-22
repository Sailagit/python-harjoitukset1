class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, tuntipalkka):
        super().__init__(etunimi, sukunimi)
        self.tuntipalkka = tuntipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tuntipalkka: {self.tuntipalkka} euroa tunnilta")

tuntipalkkainen1 = Tuntipalkkainen("Sam", "Smith", 43.8)
tuntipalkkainen1.tulosta_tiedot()