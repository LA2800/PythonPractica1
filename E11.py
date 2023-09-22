lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

lista_procesada = []

for elemento in lista_original:
    if elemento not in lista_procesada:
        lista_procesada.append(elemento)
print(lista_procesada)