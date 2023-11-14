#P20
numb=(input("Dime todo de tu numero de telefono(separalo con -): +"))
parti=numb.split("-")
prefi=parti[0]
fijo=parti[1]
subfi=parti[2]
print(f"Su número es:{fijo}")