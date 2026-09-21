# Uusi hissi on aina alimmassa kerroksessa.
# Metodi kutsuu joko kerros_ylös tai kerros_alas metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin
    def siirry_kerrokseen(self, kerros):
        while self.nykyinen != kerros:
            if self.nykyinen < kerros:
                self.kerros_ylos()
            else:
                self.kerros_alas()
    def kerros_ylos(self): # Haluaa siirtää hissiä yhden kerroksen ylöspäin
        if self.nykyinen + 1 >= self.ylin:
            self.nykyinen = self.ylin
        else:
            self.nykyinen += 1
        print(f"Nykyinen kerros: {self.nykyinen}")
    def kerros_alas(self): # Haluaa siirtää hissiä yhden kerroksen alaspäin
        if self.nykyinen - 1 <= self.alin:
            self.nykyinen = self.alin
        else:
            self.nykyinen -= 1
        print(f"Nykyinen kerros: {self.nykyinen}")

class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin # Ominaisuus
        self.ylin = ylin # Ominaisuus
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))
    def aja_hissia(self, hissin_numero, kerros):
        # Siirrä hissin numeroa vastaava hissi kerrokseen
        self.hissit[hissin_numero].siirry_kerrokseen(kerros)

# Pääohjelma
talo1 = Talo(1, 10, 3) # Kerrokset 1 - 10, 3 hissiä
talo1.aja_hissia(2, 4)