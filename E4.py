N=int(input("Ingrese un entero positivo N: "))
suma=0
if N<=0:
    print("Por favor, ingrese un entero positivo: ")
else:
    for i in range (1, N+1):
    suma +=i
print(f"La suma de los enteros desde 1 hasta {N} es :{suma}")

