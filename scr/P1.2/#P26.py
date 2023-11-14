#P26

numeros_com=int(input("Dime cuantos productos llevas? "))
produc=input("Dime cada producto separado por (,) :")
produc=produc.split(",")
for i in range (numeros_com):
    nompro=produc[i]
    print(nompro)
    