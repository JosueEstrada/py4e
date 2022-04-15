# El operador 'is' y 'is not' se puede usar en expresiones lógicas
# Similar al operador de igualdad '==' pero más fuerte
# Operador '==' solo evalúa el valor
# e.g (0 == 0.0) es True, mismo valor por la conversión de tipos de Python
# Operador 'is' evalúa el tipo y valor
# Demanda igualdad en el tipo de la variable y en el valor de la variable
# e.g (0 is 0.0) es False, uno es int y el otro float, no realiza conversión
# Se recomienda utilizarlo solo en booleanos y NoneTypes

menor = None  # Es similar al null en otros lenguajes, indica vacío, empty
print('Antes:', menor)
for valor in [3, 41, 12, 9, 74, 15]:
    if menor is None:
        menor = valor
    elif valor < menor:
        menor = valor
    print('Bucle:', valor, menor)

print('Menor:', menor)
