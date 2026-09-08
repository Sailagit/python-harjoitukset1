# Ohjelma kysyy käyttäjältä nimiä, kunnes tämä antaa tyhjänmerkkijonon
# jokaisen syötteen jälkeen ohjelma tulostaa 'uusi nimi' tai 'aiemmin syötetty',
# riippuen siitä onko nimi jo syötetty

nimet = set()

while True:
    komento = input("Anna nimi: ")

    if komento == "":
        break

    if komento in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        nimet.add(komento)
        print("Uusi nimi.")

print(nimet)




