#P25

fecha=input("Dime una fecha de tal forma dd/mm/aaaa : ")
cam=fecha.split("/")
dia=cam[0]
mes=cam[1]
año=cam[2]
print(f"""El dia dicho es {dia}.
El mes dicho es {mes}.
El año dicho es {año}.""")