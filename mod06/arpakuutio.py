# Annetaan luku, monta arpakuutiota heitetään
# Ohjelma laskee kaikkien arpakuutioiden yhteissumman

import random

arpakuutioiden_määrä = int(input("Kuinka monta arpakuutiota heitetään?: "))
toisto = 0
summa = 0

for toisto in range (arpakuutioiden_määrä):
   arpakuutio = random.randint(1, 6)
   toisto += 1
   summa += arpakuutio
print(f"Arpakuutioiden yhteenlaskettu summa on {summa}")
