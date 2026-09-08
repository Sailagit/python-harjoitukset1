# Ohjelma kysyy käyttäjältä kuukautta ja tulostaa sitä vastaavan vuodenajan
kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", 
            "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
järjestysnumero = int(input("Anna kuukauden järjestynumero (1-12): "))
talvi = [11, 0, 1]
kevät = [2, 3, 4]
kesä = [5, 6, 7]
syksy = [8, 9, 10]

if järjestysnumero -1 in talvi:
    vuodenaika = "talvi"
elif järjestysnumero - 1 in kevät:
    vuodenaika = "kevät"
elif järjestysnumero - 1 in kesä:
    vuodenaika = "kesä"
elif järjestysnumero - 1 in syksy:
    vuodenaika = "syksy"
print(f"{kuukaudet[järjestysnumero -1]}. Vuodenaika on {vuodenaika}. ")

