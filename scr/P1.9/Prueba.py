def menaje():
    return input("Mensaje")
def nomfunsumplus(num1,num2):
    if num1<0:
        num1=0
    if num2<0:
        num2=0
    return num1+num2

n1=int(input("Escribe un numero: "))
n2=int(input("Escribe otro: "))
print(nomfunsumplus(n1,n2))