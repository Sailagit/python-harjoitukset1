#kysy vuosiluku ja ilmoita onko karkausvuosi
#karkausvuosi on jaollinen neljällä
#Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla
vuosiluku = float(input("Anna vuosiluku: "))
if vuosiluku % 4 == 0:
    if vuosiluku % 400 == 0:
        print("Tämä vuosi on karkausvuosi")
    elif vuosiluku % 100 == 0:
        print ("Tämä vuosi ei ole karkausvuosi")
    else:
        print ("Tämä vuosi on karkausvuosi")
else:
    print ("Tämä vuosi ei ole karkausvuosi")

    