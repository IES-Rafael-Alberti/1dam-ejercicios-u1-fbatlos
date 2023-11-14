#P15

capital=float(input("Dime tu capital para el interes: "))
años=1
for i in range(3):
   interes=float(capital*0.04)
   capital=capital+interes
   años=1+i
   print(f"Tú capital tras el {años}º año es de {round(capital,2)}")
