num=int(input("Introduce el número: "))
incremento=int(input("Introduce el incremento: "))
total=int(input("Introduce el total: "))

while incremento<=0 or total<=0:
    print("Total e incremento deben ser mayor de 0")
    incremento=int(input("Introduce el incremento: "))
    total=int(input("Introduce el total: "))

print("Serie=>", end=" ")
print(num,end="-")
while num<total-1:
    num+=incremento
    if num==total-1:
        print(num, end="")
    elif num!=total-1:
        print(num, end="..")

print(f"-{total}",end="")
   
