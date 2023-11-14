def const():
   
    n=int(input("Dime un numero : "))
    while n!=0:
        sumar=float((n*(n+1))/2)
        n=n-1
    return sumar

print(const())