def mascaracteres(palabras):
    pos = 0
    for x in range(1, len(palabras)):
        if len(palabras[x]) > len(palabras[pos]):
            pos = x
    return palabras[pos]


# Bloque principal
lista = ["clase", "cursos", "actividades", "colegio"]
print("Palabra con mas caracteres:", mascaracteres(lista))