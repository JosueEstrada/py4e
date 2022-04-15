# Ejercicio 2: Escribe otro programa que pida una lista de números como
# la anterior y al final muestre por pantalla el máximo y mínimo de los
# números, en vez de la media.
def ex_05_02():
    max = None
    min = None
    while True:
        num = input("Ingrese un número:")
        if num == "fin":
            break
        try:
            num = int(num)
        except:
            print("Número invalido")
            continue # Finaliza la iteración actual y salta a la siguiente iteración
        if min is None or num < min:
            min = num
        if max is None or num > max:
            max = num
    print(f"Máximo = {max} , Mínimo = {min}")


ex_05_02()
