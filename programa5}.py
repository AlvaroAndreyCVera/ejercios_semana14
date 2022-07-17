def cargar_lista():
    li = []
    for x in range(5):
        val = int(input("Ingresar los valores: "))
        li.append(val)
    return li


def mayor_menor(lista):
    may = lista[0]
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
        elif lista[x] < men:
            men = lista[x]
    return [may, men]


# Bloque principal
valores = cargar_lista()
rango = mayor_menor(valores)
print("El mayor valor es", rango[0])
print("El menor valor es", rango[1])