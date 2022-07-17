def cargar():
    lista = []
    for x in range(10):
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista


def generar_listas(lista):
    valposi = []
    valnega = []
    for x in range(len(lista)):
        if lista[x] < 0:
            valnega.append(lista[x])
        else:
            if lista[x] > 0:
                valposi.append(lista[x])
    return [valposi, valnega]


def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])


# Bloque principal

li = cargar()
listaposi, listanega = generar_listas(li)
print("Lista con los valores positivos")
imprimir(listaposi)
print("Lista con los valores negativos")
imprimir(listanega)