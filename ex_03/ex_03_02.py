# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
import sys

str_horas = input("¿Cuantas horas trabajó: ")
try:
    horas = float(str_horas)
except:
    sys.exit("Error, porfavor ingresa un número")


str_tasa = input("Indique la tasa por hora: ")
try:
    tasa = float(str_tasa)
except:
    sys.exit("Error, porfavor ingresa un número")


if horas <= 40:
    pago = horas * tasa
else:
    extra = (horas - 40) * tasa * 1.5
    pago = (40 * tasa) + extra

print(f"El pago bruto es: {pago}")

# try:
#     str_horas = input("¿Cuantas horas trabajó: ")
#     horas = float(str_horas)
#
#     str_tasa = input("Indique la tasa por hora: ")
#     tasa = float(str_tasa)
# except ValueError:
#     print("Error, por favor ingresa un número válido para las horas y la tasa")
#     # salir del programa u otras acciones adecuadas
