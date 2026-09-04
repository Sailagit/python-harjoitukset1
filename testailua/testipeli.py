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
päävalikko_komennot = print("Hoida kissaa. Miten haluaisit hoitaa kissaa? Ruoki, Harjaa vai Silitä: ")      
komento = input("Anna komento: ")

ruoka_lista = [ "kala", "kana", "liha" ]
while komento != "lopeta":
    if komento == 'Ruoki':
        print("Mitä ruokaa haluat antaa kissalle?: ")
        if komento in ruoka_lista:
            print("Tämä on kissan lempiruokaa")

        
        
            

        komento = input("Anna komento: ")
print("Toiminnot lopetettu.")