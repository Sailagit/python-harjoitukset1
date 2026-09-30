# ensimmäinen luokka keittiö
class Huone:
    def __init__(self, nimi,):
        self.nimi = nimi
        self.esineet = []

# toinen luokka esineet
class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

# kolmas luokka pelaaja
class Pelaaja(Huone):
    def __init__(self, käyttäjä, sijainti):
        self.käyttäjä = käyttäjä
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, huone):
        self.sijainti = huone
        print("\nSiirryit huoneeseen: ", huone.nimi)

    def kerää_esine(self, esine):
        if esine in self.sijainti.esineet:
            self.esineet.append(esine)
            self.sijainti.esineet.remove(esine)
            print(esine.nimi, "kerättiin!")
        else:
            print("Tätä esinettä ei löydy täältä")