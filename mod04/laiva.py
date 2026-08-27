#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
hytti = str(input("Laivallamme on neljä erilaista hyttiä, LUX, A, B ja C. Mistä hytistä haluaisit tietää enemmän? "))
if hytti == "LUX":
    print ("LUX on parvekkeellinen hytti yläkannella.")
elif hytti == "A":
    print ("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "B":
    print ("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti == "C":
    print ("C on ikkunaton hytti autokannen alapuolella.")
else:
    print ("Virheellinen hyttiluokka.")