## Pelaajan nimi ja ikä
käyttäjä = input("Hei! Mikä on nimesi? ")
print("Hauska tavata, " + käyttäjä + "!")
ikä = int(input("Kerrotko vielä ikäsi: "))

## Jos pelaaja on alle 12v peli sammuu
if ikä < 12:
    print("Olet alaikäinen, peli sammutetaan")
else:
    print("Tervetuloa!")

    # Lista, johon esineet tallennetaan
    esineet = []

    # Funktio 1: kysyy esineitä ja lisää ne listaan
    def lisaa_esine():
        esine = input("Minkä esineen haluat lisätä tavaralistaan? ")
        esineet.append(esine)
        print(esine + " lisättiin listaan!")

    # Funktio 2: tulostaa listan sisällön
    def nayta_esineet():
        print("Tavaralistasi:")
        
        if len(esineet) == 0:
            print("Lista on tyhjä.")
        else:
            for esine in esineet:
                print("- " + esine)

    # Funktio 3: porkkanan kokkaaminen
    def kokkaa_porkkana():
        print("Kokataan porkkana!")
        
        komento = input(
            "Mitä tehdään ensin: pese, kuori tai pilko? Anna komento: "
        )

        while komento != "lopeta":
            if komento == "pese":
                print("Suoritan toiminnon: " + komento)
                print("Porkkana on pesty.")

            elif komento == "kuori":
                print("Suoritan toiminnon: " + komento)
                print("Porkkana on kuorittu.")

            elif komento == "pilko":
                print("Suoritan toiminnon: " + komento)
                print("Porkkana on pilkottu.")

            else:
                print("En ymmärtänyt komentoa.")

            komento = input("Anna komento tai kirjoita lopeta: ")

        print("Porkkana on kokattu!")

    # Päävalikko
    komento = ""

    while komento != "lopeta":
        print("\n--- PÄÄVALIKKO ---")
        print("1 - Lisää esine")
        print("2 - Näytä esineet")
        print("3 - Kokkaa porkkana")
        print("lopeta - Lopeta peli")

        komento = input("Valitse toiminto: ")

        if komento == "1":
            lisaa_esine()

        elif komento == "2":
            nayta_esineet()

        elif komento == "3":
            kokkaa_porkkana()

        elif komento == "lopeta":
            print("Peli lopetetaan.")

        else:
            print("Virheellinen komento. Yritä uudelleen.")


