lentoasemat = [
    {"lentoasema": "Helsinki-Vantaa", "ICAO-koodi": "EFHK"},
    {"lentoasema": "Heathrow", "ICAO-koodi": "EGLL"},
    {"lentoasema": "Istanbul", "ICAO-koodi": "LTFM"},
    {"lentoasema": "Singapore", "ICAO-koodi": "WSSS"}
]

while True:
    komento = input(
        "Haluatko syöttää uuden lentoaseman, hakea lentoasemaa vai lopettaa? "
    )

    if komento == "lopeta":
        print("Ohjelma lopetetaan.")
        break

    elif komento == "uusi":
        nimi = input("Anna lentoaseman nimi: ")
        icao = input("Anna ICAO-koodi: ")

        uusi = {
            "lentoasema": nimi,
            "ICAO-koodi": icao
        }

        lentoasemat.append(uusi)
        print("Lentoasema lisätty.")

    elif komento == "haku":
        haku = input("Anna ICAO-koodi: ")

        loytyi = False

        for lentoasema in lentoasemat:
            if lentoasema["ICAO-koodi"] == haku:
                print("Lentoasema:", lentoasema["lentoasema"])
                loytyi = True
                break

        if not loytyi:
            print("Lentoasemaa ei löytynyt.")

    else:
        print("Tuntematon komento.")

    
