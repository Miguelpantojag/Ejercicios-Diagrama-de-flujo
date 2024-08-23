#inicio
# Asignar la constante de conversion
Conversion = 0.0254
# Convertir la cantidad de tela a metros
metros = float(input("Ingresar la cantidad de tela en metros ="))
# Calcular la cantidad de tela en pulgadas
pulgadas = metros / Conversion
# Resultado
print(f"la cantidad de tela total en pulgadas es: {pulgadas:.2f}")
#FIN
