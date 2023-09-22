lista = ["Rojo", "Verde", "Blanco", "Negro", "Rosa", "Amarillo"]
indices_a_eliminar =[0,4,5]
for indice in sorted (indices_a_eliminar, reverse=True):
    if indice < len(lista):
        lista.pop(indice)
print(lista)