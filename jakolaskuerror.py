try:
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    osamäärä = luku1 / luku2 
    print(f"Lukujen osamäärä on {osamäärä: 2}")
except ValueError:
    print("Virhe: syötetty arvo ei ole kokonaisluku. Yritä uudelleen.")
except ZeroDivisionError:
    print("Virhe: Nollalla ei voi jakaa.")
