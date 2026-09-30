lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti1.tulosta_tiedot()
kirja1.tulosta_tiedot()

with open("kirjasto.txt", "a") as tiedosto:
    tiedosto.write("Pelaaja pääsi tasolle 3.")