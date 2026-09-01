#kysy vuosilukua ja kerro onko olympiavuosi
#ohjelma kysyy uudelleen,kunnes käyttäjä syöttää ei modernin o vuosiluvun
#o aina jaollinen 4
vuosi = int(input("Anna vuosiluku: "))
while vuosi >= 1896:

    if vuosi % 4 == 0:
        print("Tämä on olympiavuosi")
    else:
        print("Tämä ei ole olympiavuosi")

    vuosi = int(input("Anna vuosiluku: "))

print("Ohjelma ohi")