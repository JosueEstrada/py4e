# Ejercicio 1: Escribe un programa que lea repetidamente números hasta que el
# usuario introduzca “fin”. Una vez se haya introducido “fin”, muestra por
# pantalla el total, la cantidad de números y la media de esos números. Si el
# usuario introduce cualquier otra cosa que no sea un número, detecta su
# fallo usando try y except, muestra un mensaje de error y pasa al número
# siguiente.
def ex_05_01():
    suma = 0
    contador = 0
    promedio = 0
    while True:
        dato = input("Introduzca un número:")
        if dato == "fin":
            break
        try:
            dato = int(dato)
            contador += 1
            suma += dato
        except:
            print("Error: Entrada inválida")

    promedio = suma / contador
    print("Total | Contador | Promedio")
    print(suma, contador, promedio)


ex_05_01()
