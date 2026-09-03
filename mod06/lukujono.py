# Käyttäjä syöttää lukuja, kunnes käyttäjä syöttää tyhjän merkkijonon

luvut = []

luku = input("Anna luku tai lopeta painamalla Enter: ")

while luku != "":
    luvut.append(int(luku))
    luku = input("Anna luku tai lopeta painamalla Enter: ")

luvut.sort(reverse=True)
# Ohjelma tulostaa 5 suurinta suuruusjärjestyksessä
for luku in luvut [:5]:
    print(luku)

