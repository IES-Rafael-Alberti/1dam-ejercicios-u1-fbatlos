#27
nombre_producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio unitario del producto: "))
numero_unidades = int(input("Introduce el número de unidades: "))
costo_total = precio_unitario * numero_unidades
cadena_resultado = "{} tiene un precio unitario de {:09.2f}, {03d} unidades y un costo total de {:011.2f}".format(
    nombre_producto, precio_unitario, numero_unidades, costo_total)
print(cadena_resultado)