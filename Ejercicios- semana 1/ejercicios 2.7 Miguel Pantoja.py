# Datos
try:
    litros = float(input("Ingrese la cantidad de litros producidos: "))
    precio_por_galon = float(input("Ingrese el precio por galón: "))

    # Verificar entradas validas
    if litros < 0 or precio_por_galon < 0:
        print("Los valores de litros y precio por galón deben ser positivos.")
    else:
        # Cálcular
        galones = litros / 3.875
        total_pago = galones * precio_por_galon
        
        # Salida
        print("El total a recibir es: $", round(total_pago, 2))

except ValueError:
    print("Por favor, ingrese un valor numérico válido.")
    