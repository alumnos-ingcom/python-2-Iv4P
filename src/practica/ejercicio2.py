################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números,
retornando los valores como una tuple.

Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""
# Reemplazar por las funciones del ejercicio
def estadisticas(lista):
    """
    Esta funcion ordena una lista de mayor a menor 
    para luego usar las posiciones 0 y -1 
    Y realiza el promedio de la lista
    """
    promedio = 0
    i = 0
    while i <= len(lista):
        j = 1
        while j <= len(lista) -1:
            if lista[j-1] < lista[j]:
                box = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = box
            j = j + 1
        i = i + 1
    i = 1 
    while i <= len(lista):
        promedio = promedio + lista[i-1]
        i = i + 1
    promedio = promedio / len(lista)
    return lista[0], lista[-1], promedio
    
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista = []
    flag = False
    while flag == False:
        num = int(input("Ingrese numero: "))
        lista.append(num)
        flag = bool(input("Ingrese enter para continuar o una letra para finalizar: "))
    res = estadisticas(lista)
    print(f"El maximo es {res[0]}, el minimo es {res[1]} y el promedio es {res[-1]}")


if __name__ == "__main__":
    principal()
