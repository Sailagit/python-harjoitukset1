#peli arpoo kokonaisluvun väliltä 1..10
#peli kysyy lukua niin kauan kunnes pelaaja arvaa oikein
#liian suuri arvaus, liian pieni arvaus, tai oikein

import random

luku = random.randint(1, 10)
arvaus = 0

while arvaus != luku:
    arvaus = int(input("Arvaa luku 1-10: "))

    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein")