# Ohjelma kysyy gallonien määrää ja muuttaa ne litroiksi
# Muunnos on tehtävä aliohjelmaa käyttäen
# Muuntaminen jatkuu kunnes syöttää negatiivisen
# 1 gallon on 3,785 litraa

def gallon_litroina(gallonat):
    litra= gallonat * 3.785
    return litra

while True:

    gallonat = float(input("Anna gallon määrä: "))
    litra = gallon_litroina(gallonat)

    if gallonat < 0:
        break

    print(f"{litra} litraa.")