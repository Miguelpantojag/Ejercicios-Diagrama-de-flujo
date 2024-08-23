# Datos
def calcular_area_terreno(A, B, C):
    # Calcular el area del triángulo
    area_triangulo = 0.5 * B * (A - C)
    
    # Calcular el area del rectángulo
    area_rectangulo = B * C
    
    # Calculos finales

    # Calcular el area total del terreno
    area_total = area_triangulo + area_rectangulo 
    return area_total

# Solicitar al usuario que ingrese los valores de A,B,C
A = float(input("Ingrese la altura total A: "))
B = float(input("ingrese la altura total B: "))
C = float(input("Ingrese la altura total C: "))
 # Calcular y mostrar el area total del terreno
area = calcular_area_terreno(A,B,C)
print(f"El area total del terreno es: {area} metros cuadrados")