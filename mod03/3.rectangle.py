import math

kanta = input("Anna suorakulmion kanta: ")
korkeus= input("Anna suorakulmion korkeus: ")

kanta = float(kanta)
korkeus = float(korkeus)

pinta_ala = kanta * korkeus
piiri = kanta * 2 + korkeus * 2
print(f"Suorakulmion pinta-ala on: {pinta_ala:6.2f} ja piiri on {piiri:6.2f}")