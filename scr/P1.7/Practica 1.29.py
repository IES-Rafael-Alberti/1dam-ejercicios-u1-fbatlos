#inicio
#escribe nombre y edad
#lee nom,edad
#si nom=" " hacer
#   nom="Desconocido"
#mientras edad<0 or edad>125
#      escribe Edad no valida
#escribe Te llamas nom y tienes edad años, te quedan aún 125-edad años por cumplir"
#fin
nom=input("Dime tu nombre: ")
edad=int(input("Dime tu edad: "))

if nom==" ":
    nom="Desconocido"
while edad<0 or edad>125:
    print("ERROR")
    edad=int(input("Dime tu edad: "))   

print(f"Te llamas {nom} y tienes {edad} años, te quedan aún {125-edad} años por cumplir")