# Pääohjelma kysyy kahden pitsan halkaisijaa ja hintaa.
import math

#funktio laskee yksikköhinnan
def yksikköhinta(halkaisija, hinta):
    säde = halkaisija / 2 / 100
    pinta_ala = math.pi * säde ** 2

    return hinta / pinta_ala

pitsa1 = float(input("Anna ensimmäisen pitsan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pitsan hinta (e): "))

pitsa2 = float(input("Anna toisen pitsan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pitsan hinta (e): "))

#lasketaan kumpi antaa paremman yksikköhinnan
yksikköhinta1 = yksikköhinta(pitsa1, hinta1)
yksikköhinta2 = yksikköhinta(pitsa2, hinta2)

# tulostaa kumpi pitsa on parempi
if yksikköhinta1 < yksikköhinta2:
    print("Ensimmäinen pitsa antaa paremman vastineen rahalle.")
elif yksikköhinta2 < yksikköhinta1:
    print("Toinen pitsa antaa paremman vastineen rahalle.")
else:
    print("Pitsat antavat saman vastineen rahalle.")