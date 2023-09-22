edad= int(input("Por favor, ingrese su edad: "))
if edad <4:
    precio_entrada =0
elif 4<= edad <= 18:
    precio_entrada= 5
else:
    precio_entrada=10
print(f"El precio de la entrada es ${precio_entrada}")

