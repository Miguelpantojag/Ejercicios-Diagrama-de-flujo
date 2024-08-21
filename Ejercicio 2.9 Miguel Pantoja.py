# funcion para calcular sueldo semanal de un trabajador
def calcular_sueldo_semanal(horas_trabajadas, pago_por_hora):
    # Calcular el sueldo semanal
    sueldo_semanal = horas_trabajadas * pago_por_hora 
    return sueldo_semanal 
# Solicitar al trabajador ingresar sus horas trabajadas y su pago por hora 
horas_trabajadas = float(input("ingrese sus horas de trabajo=50"))
pago_por_hora = float(input("ingrese el pago por hora=")) 
# Calcular el sueldo segun la funcion dada
sueldo = calcular_sueldo_semanal(horas_trabajadas, pago_por_hora)
# Mostrar el resultado en la pantalla
print(f"el sueldo semanal es :{sueldo}pesos=") 
