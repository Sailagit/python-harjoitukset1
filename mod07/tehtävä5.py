#tulostaa alkuperäisen listan 
#tulostaa parilliset listan

def parilliset_luvut(luvut):
    parilliset = []

    for i in luvut:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

def kaikki_luvut(luvut):
   print(f"Kaikki listan luvut: {lista}")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parilliset = parilliset_luvut(lista)
kaikki = kaikki_luvut(lista)

print(f"Listan parilliset ovat {parilliset}.")