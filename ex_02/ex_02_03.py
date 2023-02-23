# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

str_horas = input("¿Cuantas horas trabajó: ")
str_tasa = input("Indique la tasa por hora: ")

horas = int(str_horas)
tasa = float(str_tasa)
pago = horas * tasa

print(f"El pago bruto es: {round(pago)}")

