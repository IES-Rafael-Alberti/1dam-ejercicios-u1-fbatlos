#Inicio

#	Escribe "Introduce un número: "
#	Lee num
#	
#	Mientras (num < 1 or num > 10)
#		Escribe "Inténtalo otra vez! (1-10): "
#		Lee num
#	Escribe "Correcto!"
#	
#Fin

numero=int(input("Introduce un número: "))
while(numero<1 or numero>10):
    numero=int(input("Inténtalo otra vez! (1-10): "))
print("CORRECTO!")