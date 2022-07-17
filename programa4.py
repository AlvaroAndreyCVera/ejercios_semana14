def cargar_datos():
    sueldo = []
    for x in range(10):
        valor = int(input("Ingrese el sueldo del empleado: "))
        sueldo.append(valor)
    return sueldo


def imprimir(lista):
    print("Los sueldos superiores a $4000 son:")
    for x in range(len(lista)):
        if lista[x] > 4000:
            print(lista[x])


def promedio_sueldo(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    promedio = suma // 10
    return promedio


def otros_sueldos(lista):
    prom = promedio_sueldo(lista)
    print("El promedio del sueldo de los empleados es: ", prom)
    print("Los sueldos menores al promedio son:")
    for x in range(len(lista)):
        if lista[x] < prom:
            print(lista[x])


# Bloque principal
li = cargar_datos()
imprimir(li)
promedio_sueldo(li)
otros_sueldos(li)