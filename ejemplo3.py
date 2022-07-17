def producto(lista):
    prod = 1
    for x in range(len(lista)):
        prod = prod * lista[x]
    return prod


# Bloque principal
lista = [1, 2, 3, 4, 5]
print("Lista: ", lista)
print("Multiplicación de todos sus elementos: ", producto(lista))