## asiakkaan ikä
## asiakkaan rotu
## tulosta juomalista
ikä = int(input("Anna ikäsi: "))
laji = input("Minkä lajinen olet?")
print("Voit tilata seuraavat juomat: ")
print("kahvi")
if laji == "ihminen" and ikä >= 18:
    print(" viini")
elif laji == "tonttu" and ikä >= 100:
    print(" olut")
elif laji == "robotti":
    print(" öljy")