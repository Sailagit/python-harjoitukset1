# Tee luokka inventaario, inventaariolla on loitsut lista ja sanakirja reppu
# Konstruktori lisää loitsut listaan  kaksi tavaraa
# Konstruktori saa parametrina toisen listan loitsuja, myös ne lisätään
# olion loitsut listaan. Luo pääohjelmassa inventaario-olio, tarkista että toimii.
# Tee metodi, jolla käyttäjä voi lisätä reppuun tavaroita. Kunkin tavaran nimi on 
# sanakirjan avain, arvoksi tulee tavaran laatu (hyvä, keskinkertainen, huono tms.)
# Ensin kaikki tavarat voivat olla samaa laatua, esim "hyvä"
# Tee metodi, joka tulostaa kauniisti repun sisällön eli tavaroiden nimet ja laadun.
# Muuta koodi niin, että tavaran laatu on monikko (=tuple)
class Inventaario:
    def __init__(self):
        self.loitsut = []
        self.reppu = {}

    def loitsu(self, loitsu):
        self.loitsut.append(loitsu)

inventaario = Inventaario()
lisätään_loitsu = input("Anna loitsu: ")
inventaario.loitsu(lisätään_loitsu)

print(inventaario.loitsut)