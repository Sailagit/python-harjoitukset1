#ohjelma joka arpoo pisteet neliön sisälle
import random
import math

#ympyrän säde
ympyrä_säde = 1

# kysytään käyttäjältä arvottavien pisteiden määrä
pisteiden_määrä = int(input("Kuinka monta pistettä?: "))

ympyrän_pisteet = 0
toistot = 0

while toistot < pisteiden_määrä:
# Arpoo pisteet neliön sisälle
    x = random.uniform(-1, 1)
    y = random.uniform(-1,1)

#tarkistetaan onko piste ympyrän sisällä
    n= ympyrän_pisteet
    if x ** 2 + y ** 2 < 1:
        ympyrän_pisteet += 1
    toistot += 1
    N = pisteiden_määrä

#piin likiarvo
pi = 4 * ympyrän_pisteet / N

print("Piin likiarvo on:", pi)



