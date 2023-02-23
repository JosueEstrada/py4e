# No llamar los archivos como el nombre de una
# libreria, o dara error en la importacion:
# random.py <- no utilizar nombre así...
import random

for i in range(10):
    print(random.random())
