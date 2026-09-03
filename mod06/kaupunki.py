# Kysy 5 kaupungin nimi
# Tulostaa nimet allekkain siinä järjestyksessä, kun ne on syötetty

kaupungit = []

for syöte in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

for kaupunki in kaupungit:
    print(f"{kaupunki}")