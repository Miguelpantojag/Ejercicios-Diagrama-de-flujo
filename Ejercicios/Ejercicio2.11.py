# INICIO
# Obtener las dimensiones de la alberca
A = float(input("Introducir el ancho de la alberca en metros = "))
L = float(input("Introducir el largo de la alberca en metros = "))
P = float(input("Introducir la profundidad de la alberca en metros = "))
# Calcular el volumen de la alberca
Volumen  = A * L * P
# Costo por metro cubico de agua 
costo_metro3 = float(input("Ingresar el costo por metro cubico de agua = "))
# Pago total
Pago_total = Volumen * costo_metro3

print(f"el pago total por el consumo de agua es = ${Pago_total:.2f}")
