# Exercise 5: Write a program which prompts the user for a Celsius
# temperature, convert the temperature to Fahrenheit, and print out the
# converted temperature.

str_input = input("Ingrese Temperatura en Celsius: ")
cels = float(str_input)
fahr = (cels * 9 / 5) + 32
print(f"Temperatura en Fahrenheit es {fahr}ºF")
