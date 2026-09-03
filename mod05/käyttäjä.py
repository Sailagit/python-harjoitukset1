# ohjelama kysyy käyttäjätunnusta ja salasanaa
# molempien pitää olla oikein, muuten kysyy uudelleen
# väärät tiedot saa syöttää 5 kertaa
# jos syöte on oiken tulosta 'Tervetuloa'
# jos syöte on mennyt 5 kertaa väärin tulosta 'Pääsy evätty'
# käyttäjätunnus on python ja salasana on rules

käyttäjätunnus = 'python'
salasana = 'rules'

yritykset = 0

while yritykset < 5:
    user = input("Anna käyttäjätunnus ja salasana: ")

    if user == käyttäjätunnus + " " + salasana:
        print("Tervetuloa.")
        break
    yritykset += 1
    print("Väärä käyttäjätunnus tai salasana.")

    if yritykset == 5:
        print("Pääsy evätty.")
