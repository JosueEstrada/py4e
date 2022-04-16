# Ejercicio 5: Toma el siguiente código en Python que almacena una cadena:
# str = 'X-DSPAM-Confidence:0.8475'
# Utiliza find y una parte de la cadena para extraer la porción de la cadena
# después del carácter dos puntos y después utiliza la función float para
# convertir la cadena extraída en un número de punto flotante.
def ex_06_06():
    str = 'X-DSPAM-Confidence:0.8475'
    # print(str.find(":"))  # Posición en la cadena : 18
    # print(str[18:])  # Imprime la cadena desde la posición 18 hast el final
    # Para el número hay que agregar una posición más para que convierta la
    # cadena después de los ':' hasta el final
    # Otra forma para evitar confusiones
    index = str.find(":") + 1  # Posición donde empieza el primer número
    numero = str[index:]  # Extrae la cadena
    numero = float(numero)  # Conversión de string a float
    # Se puede escribir en una sola línea de la siguiente manera
    # numero = float(str[str.find(":") + 1:])
    # print(type(numero)) # Señala el tipo de dato
    print(f"Número: {numero}")


ex_06_06()
