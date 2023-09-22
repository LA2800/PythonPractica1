# solicita al usuario el costo de la comida
costo_comida = float(input("Ingrese el costo de la comida: $"))

porcentaje_propina = float(input("Ingrese el porcentaje de propina a dejar: "))

propina = (porcentaje_propina / 100) * costo_comida

print(f"Debería dejar ${propina}")
