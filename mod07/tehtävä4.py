# Pääohjelma, jossa luotu lista ja funktio, joka laskee listan summan.

def lukujen_summa(luvut):
    s = 0
    for i in luvut:
        s += i
    return s

lista = [10, 20, 30, 40, 50, 60,]
summa = lukujen_summa(lista)

print(f"Lukujen summa on {summa: .2f}.")