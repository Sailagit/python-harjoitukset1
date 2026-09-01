#muuntaa tuumat senttimetreiksi
#muuntaa niin kauan kunnes käyttäjä antaa negatiivisen tuuman
# 1 tuuma = 2,54cm
cm = float(input("Anna luku senttimetreinä: "))
tuuma = 0

while tuuma >= 0:
    tuuma = (cm * 2.54)

    if tuuma >= 0:
        print(f"{tuuma}")
        cm = float(input("Anna luku senttimetreinä: "))
    if tuuma < 0:
        break
print("Luku on negatiivinen")
