hora_ingresada =input("Por favor, ingrese una hora en formato HH:MM")
hour, minutes =map (int, hora_ingresada.split(':'))
def es_hora_de_comida(hour,minutes,inicio,fin):
    hour_decimal=hour+minutes /60
    return inicio <=hour_decimal <= fin
if es_hora_de_comida(hour,minutes,7,8):
    print("Es hora de desayunar.")
elif es_hora_de_comida(hour,minutes,12,13):
    print("Es hora de almorzar.")
elif es_hora_de_comida(hour, minutes,18,19):
    print("Es hora de cenar.")
else:
    print("No es hora de comer")
