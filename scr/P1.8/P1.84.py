#Inicio
#	num = 3
#	Escribe "Dime cuantos números debe tener la serie: "
#	Lee total
#	cont = 1
#	Mientras (cont <= total) hacer
#		Escribe num
#		Si (cont < total) entonces
#			Escribe " "
#		num = num + 3
#		cont = cont + 1	
#Fin
num=3
total=int(input("Dime cuantos números debe tener la serie: "))
cont=1
while cont <= total :
    print(num)
    if cont<total:
        print("")
    num=num+3
    cont=cont+1