#P5
precio_sin_iva = float(input("Ingresa el precio: "))
porcentaje_iva = float(input("Ingresa el porcentaje de IVA: "))
precio_final = precio_sin_iva * (1 + porcentaje_iva / 100)
print("El precio final es: ", precio_final, "€")
