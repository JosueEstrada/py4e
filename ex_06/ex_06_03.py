# Ejercicio 3: Encapsula este código en una función llamada cuenta, y
# hazla genérica de tal modo que pueda aceptar una cadena y una letra
# como argumentos.
def cuenta(cadena):
    contador = 0
    for e in cadena:
        contador += 1
    print(f"Palabra: {cadena}, Número de carácteres: {contador}")


cuenta("a")
cuenta("Hola")
cuenta("Monty Python")
