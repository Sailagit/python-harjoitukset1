#kirjoita ohjelma, joka tulostaa kolmella jaolliset luvut 1....1000 väliltä
luku = 0
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1
print("Kaikki numerot käyty läpi")
