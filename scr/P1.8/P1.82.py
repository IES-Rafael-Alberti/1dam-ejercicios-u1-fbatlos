#Inicio
#
#	Escribe "Introduce un número: "
#	Lee x
#	Escribe "Introduce otro: "
#	Lee y
#	
#	Si (x >= y) entonces
#		numIni = x - 1
#		numFin = y
#	Sino
#		numIni = y - 1
#		numFin = x
#		
#	Para i en (numIni...numFin) hacer
#		Si (i == numFin) entonces
#			Escribe "i"
#          sino
#           Escribe "i,al fina -"
#Fin
x=int(input("Introduce un número: "))
y=int(input("Introduce otro: "))
if x>=y : 
    numIni=y
    numFin=x
else:
    numIni=x
    numFin=y

for i in range(numIni,numFin+1):
    if(i==numFin):
        print(i,end="")
    else:
        print(i,end="-")