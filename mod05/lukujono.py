# lopuksi tulostaa pienimmän annetun luvun ja isoimman

pienin = None
suurin = None

numero = input("Anna luku: ")

while numero != "":
    numero = float(numero)

    if pienin is None or numero < pienin:
        pienin = numero

    if suurin is None or numero > suurin:
        suurin = numero
    numero = input("Anna luku: ")
    
if pienin is not None:
    print(f"Suurin numero: {suurin}")
    print(f"Pienin numero: {pienin}")
