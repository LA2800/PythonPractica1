numero_1= float(input("Ingrese el primer número 1:"))
numero_2= float(input("Ingrese el segundo número 2:"))

print("Menú: ")
print("1. sumar los dos números")
print("2. restar el segundo número al primero")
print("3. multiplicar los dos números")

opcion=int(input("Por favor, seleccione una opción (1/2/3): "))
if opcion==1:
    resultado=numero_1+numero_2
    print(f"La suma de {numero_1} y {numero_2} es:")
elif opcion==2:
    resultado=numero_1-numero_2
    print(f"La resta de {numero_1} con {numero_2} es: ")
elif opcion==3:
    resultado=numero_1*numero_2
    print(f"La multiplicación de {numero_1} y {numero_2} es :")
else:
    print ("Opción invalida")

    