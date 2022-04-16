# Ejercicio 4: Hay un método de cadenas llamado count que es similar a la
# función del ejercicio previo. Lee la documentación de este método en:
# https://docs.python.org/library/stdtypes.html#string-methods Escribe una
# invocación que cuenta el número de veces que una letra aparece en “banana”.
# str.count(sub[, start[, end]]) Return the number of non-overlapping
# occurrences of substring sub in the range [start, end]. Optional arguments
# start and end are interpreted as in slice notation.
def cuenta(cadena, buscar):
    contador = cadena.count(buscar)
    print(f"'{buscar}' aparece {contador} veces en '{cadena}'")


cuenta("banana", "a")
cuenta("amor", "s")


