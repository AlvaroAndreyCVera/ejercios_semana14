def mayor(lista):
    may = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may


def menor(lista):
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men


# Bloque Principal
li = []
for x in range(5):
    valores = int(input("Ingrese los valores de la lista: "))
    li.append(valores)
print("El mayor valor es ", mayor(li))
print("El menor valor es ", menor(li))