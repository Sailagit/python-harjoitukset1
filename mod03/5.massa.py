import math
leiviskä = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))
talent = float(leiviskä * 20)
nail = float((talent + naula)*32)
grammat = ((nail + luoti)*13,3)
print (f"Massa nykymittojen mukaan on {grammat} mg")
