##pelaajan nimi ja ikä
käyttäjä = input("Hei! Mikä on nimesi? ")
print("Hauska tavata, " + käyttäjä + "!")
ikä = int(input("Kerrotko vielä ikäsi: "))

##jos pelaaja on alle 12v peli sammuu
if ikä < 12:
    print("Olet alaikäinen, peli sammutetaan")
else:
    print("Tervetuloa")

päävalikko = print("Päävalikko") 
komento = input("Kokataan porkkana. Mitä tehdään esin, pese, kuoria tai pilko? Anna komento: ")
while komento != "lopeta":
    if komento == 'pese':
        print("Suoritan toiminnon: " + komento)
        print("Porkkana on pesty")

    elif komento == 'kuori':
        print("Suoritan toiminnon: " + komento)
        print("Porkkana on kuorittu")

    elif komento == 'pilko':
        print("Suoritan toiminnon: " + komento)
        print("Porkkana on pilkottu.")

    komento = input("Anna komento tai kirjoita lopeta: ")
print("Porkkana on kokattu.")