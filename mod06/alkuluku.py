# Ohjelma kysyy käyttäjältä kokonaislukua ja ilmoittaa onko luku alkuluku

luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print("Tämä ei ole alkuluku")
else:
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            print("Tämä ei ole alkuluku")
            break
    else:
        print("Tämä on alkuluku")

