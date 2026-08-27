sukupuoli = input("Anna biologinen sukupuolesi: ")
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvosi: "))
if sukupuoli == "nainen" and 117 <= hemoglobiiniarvo < 175:
    print ("Arvosi ovat normaalit. Hienoa!")
elif sukupuoli == "nainen" and hemoglobiiniarvo <= 116:
    print ("Sinulla on liian matala hemoglobiiniarvo")
elif sukupuoli == "nainen" and hemoglobiiniarvo >= 176:
    print ("Sinulla on liian korkea hemoglobiiniarvo")
elif sukupuoli == "mies" and 134 <= hemoglobiiniarvo < 195:
    print ("Arvosi ovat normaalit. Hienoa!")
elif sukupuoli == "mies" and hemoglobiiniarvo <= 133:
    print ("Sinulla on liian matala hemoglobiiniarvo")
elif sukupuoli == "mies" and hemoglobiiniarvo >= 196:
    print ("Sinulla on liian korkea hemoglobiiniarvo")
else:
    print ("Virheellinen sukupuoli.")