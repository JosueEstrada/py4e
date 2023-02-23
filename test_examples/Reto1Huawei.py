cadena = input("Ingrese carácter:")
if cadena.isdigit():
    print("Es número")
elif cadena.islower():
    print("Es letra minúscula")
elif cadena.isupper():
    print("Es letra mayúscula")
else:
    print("No es letra ni número")

