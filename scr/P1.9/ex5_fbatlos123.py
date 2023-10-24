"""
Crea un algoritmo en pseudocódigo y pásalo también a un programa en Python que pida los días totales trabajados en la vida laboral y te transforme esos días a años, meses y días.

Para este programa vamos a considerar que todos los años tienen 365 días y todos los meses 30 días.

Debe cumplir lo siguiente:

- La palabra año, mes y día irá en plural o singular dependiendo de su cantidad.

- No puede introducir un valor negativo para los días. Si lo hace, debéis dar un mensaje de error y volver a pedir los días trabajados hasta que introduzca un número positivo (el 0 también es válido).

Ejemplo 1:

> Introduzca los días trabajados: 1347
> Ha cotizado 3 años, 8 meses y 12 días.

Ejemplo 2:

> Introduzca los días trabajados: 31
> Ha cotizado 0 años, 1 mes y 1 día.

Ejemplo 3:

> Introduzca los días trabajados: -230
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: -33
> *** Error - el valor no puede ser negativo ***
> Introduzca los días trabajados: 0
> Ha cotizado 0 años, 0 meses y 0 días.


Inicio
    escribe Introduzca los días trabajados: 
    lee total_de_dias
    mientras total_de_dias<0 hacer
        escribe Error - el valor no puede ser negativo
        lee total_de_dias
    si total_de_dias==0 entonces
        escribe "Ha cotizado 0 años, 0 meses y 0 días."
    sino 
        años=total_de_dias//365
        resto_dias=total_de_dias%365
        mes=resto_dias//30
        dias=resto_dias%30
        resultado = "En su vida laboral, usted ha trabajado "
        si años >= 0 entonces
          resultado = resultado + str(años)
        si años == 1 entonces
            resultado = resultado + " año, "
        sino
            resultado = resultado + " años, "      
        si mes >= 0 entonces
          resultado = resultado + str(mes)
        si mes == 1 entonces
            resultado = resultado + " mes, "
        sino
            resultado = resultado + " meses, " 
        si dias >= 0 entonces
          resultado = resultado + str(años)
        si dias == 1 entonces
            resultado = resultado + " dís, "
        sino
            resultado = resultado + " días, " 
lee resultado
Fin
"""
total_de_dias=int(input("Introduzca los días trabajados: "))
while total_de_dias<0:
    total_de_dias=int(input("Error - el valor no puede ser negativo"))
if total_de_dias==0:
    print("Ha cotizado 0 años, 0 meses y 0 días.")
else:
    años=total_de_dias//365
    resto_dias=total_de_dias%365
    mes=resto_dias//30
    dias=resto_dias%30
    resultado = "En su vida laboral, usted ha trabajado "
    if años >= 0:
     resultado += str(años)
    if años == 1:
        resultado += " año, "
    else:
        resultado += " años, "
    if mes >= 0:
        resultado += str(mes)
    if mes == 1:
        resultado += " mes, "
    else:
        resultado += " meses, "
    if dias >= 0:
        resultado += str(dias)
    if dias == 1:
        resultado += " día"
    else:
        resultado += " días"
print(resultado)