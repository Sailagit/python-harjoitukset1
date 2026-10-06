from luokat import Huone, Esine, Pelaaja

## Pelaajan nimi ja ikä
käyttäjä = input("Hei! Mikä on nimesi? ")
print("Hauska tavata, " + käyttäjä + "!")
ikä = int(input("Kerrotko vielä ikäsi: "))

def lue_intro():
    try:
        with open("Porkkanapeli/peli/intro.txt", "r", encoding="utf-8") as tiedosto:
            intro = tiedosto.read()
        return intro
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")

## Jos pelaaja on alle 12v peli sammuu
if ikä < 12:
    print("Olet alaikäinen, peli sammutetaan")
    exit()
else:
    print(lue_intro())

keittiö = Huone("Keittiö")
varasto = Huone("Varasto")
ruokakomero = Huone("Ruokakomero")
esine1 = Esine("veitsi", 1)
esine2 = Esine("kuorimaveitsi", 0.5)
esine3 = Esine("leikkuulauta", 2)
varasto.esineet.append(esine1)
ruokakomero.esineet.append(esine2)
keittiö.esineet.append(esine3)
pelaaja1 = Pelaaja(käyttäjä, keittiö)

def lue_ohjeet():
    try:
        with open("Porkkanapeli/peli/ohjeet.txt", "r", encoding= "utf-8") as tiedosto:
            ohjeet = tiedosto.read()
        return ohjeet
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")
print(lue_ohjeet())

def näytä_esineet():
    print("\nTyövälineesi:")

    if len(pelaaja1.esineet) == 0:
        print("Sinulla ei ole vielä yhtään esinettä.")
    else:
        for esine in pelaaja1.esineet:
            print("-", esine.nimi, "(", esine.paino, "kg)")

import json

def tallenna_peli():
    tallennus = {
        "käyttäjä": pelaaja1.käyttäjä,
        "sijainti": pelaaja1.sijainti.nimi,
        "esineet": []
    }

    for esine in pelaaja1.esineet:
        tallennus["esineet"].append(esine.nimi)

    with open("tallennus.json", "w") as tiedosto:
        json.dump(tallennus, tiedosto)

    print("Peli tallennettu!")

def lataa_peli():
    try:
        with open("tallennus.json", "r") as tiedosto:
            tallennus = json.load(tiedosto)

        pelaaja1.käyttäjä = tallennus["käyttäjä"]

        if tallennus["sijainti"] == "Keittiö":
            pelaaja1.sijainti = keittiö
        elif tallennus["sijainti"] == "Varasto":
            pelaaja1.sijainti = varasto
        elif tallennus["sijainti"] == "Ruokakomero":
            pelaaja1.sijainti = ruokakomero

        pelaaja1.esineet = []

        for esineen_nimi in tallennus["esineet"]:
            if esineen_nimi == "veitsi":
                pelaaja1.esineet.append(esine1)
            elif esineen_nimi == "kuorimaveitsi":
                pelaaja1.esineet.append(esine2)
            elif esineen_nimi == "leikkuulauta":
                pelaaja1.esineet.append(esine3)

        print("Peli ladattu!")

    except FileNotFoundError:
        print("Tallennettua peliä ei löytynyt.")


def näytä_huoneen_esineet():
    print("\nHuoneessa", pelaaja1.sijainti.nimi, "on:")

    if len(pelaaja1.sijainti.esineet) == 0:
        print("Huoneessa ei ole esineitä.")
    else:
        for esine in pelaaja1.sijainti.esineet:
            print("-", esine.nimi)



    # Funktio 1: kysyy esineitä ja lisää ne listaan
def lisaa_esine():
    näytä_huoneen_esineet()

    nimi = input("Minkä esineen haluat kerätä? ")

    for esine in pelaaja1.sijainti.esineet:
        if esine.nimi == nimi:
            pelaaja1.kerää_esine(esine)
            return

    print("Tällaista esinettä ei löytynyt.")

    # Funktio 3: porkkanan kokkaaminen
def kokkaa_porkkana():
    print("Kokataan porkkana!")
    
    komento = input("Mitä tehdään ensin: pese, kuori tai pilko? Anna komento: ")

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

        komento = input("Anna komento tai kirjoita lopeta, lopettaaksesi kokkauksen: ")

    print("Porkkana on kokattu!")

def liiku():
    print("\nMinne haluat mennä?")
    print("1 - Keittiö")
    print("2 - Varasto")
    print("3 - Ruokakomero")

    valinta = input("Valitse huone: ")

    if valinta == "1":
        pelaaja1.liiku(keittiö)

    elif valinta == "2":
        pelaaja1.liiku(varasto)

    elif valinta == "3":
        pelaaja1.liiku(ruokakomero)

    else:
        print("Virheellinen valinta.")

# Päävalikko

print("Haluatko aloittaa uuden pelin vai jatkaa tallennettua peliä?")
print("1 - Uusi peli")
print("2 - Jatka peliä")

valinta = input("Valitse: ")

if valinta == "2":
    lataa_peli()


lue_intro()
lue_ohjeet()

komento = ""

while komento != "lopeta":

    print("\n--- PÄÄVALIKKO ---")
    print("Olet huoneessa:", pelaaja1.sijainti.nimi)
    print("Mitä haluat tehdä?")
    print("1 - Kerää esine")
    print("2 - Näytä omat esineet")
    print("3 - Näytä huoneen esineet")
    print("4 - Liiku toiseen huoneeseen")
    print("5 - Kokkaa porkkana")
    print("6 - Tallenna peli")
    print("lopeta - Lopeta peli")

    komento = input("Valitse toiminto: ")

    if komento == "1":
        lisaa_esine()

    elif komento == "2":
        näytä_esineet()

    elif komento == "3":
        näytä_huoneen_esineet()

    elif komento == "4":
        liiku()

    elif komento == "5":
        kokkaa_porkkana()

    elif komento == "6":
        tallenna_peli()

    elif komento == "lopeta":
        print("Peli lopetetaan.")

    else:
        print("Virheellinen komento. Yritä uudelleen.")


