################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""

# Reemplazar por las funciones del ejercicio
def super_puestos(lista1, lista2):
    """ 
    Compara dos lista, si hay una letra igual
    verifica si el resto de chars son iguales
    """
    cont = 0
    for i in range(lista1.index(lista2[0]), (len(lista2))):
            if lista1[i]==lista2[i]:
                cont = cont + 1
    posicion = lista1.index(lista2[0])
    return cont, posicion

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista1 = ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
    lista2 = ['H','o', 'l', 'a']
    res = super_puestos(lista1, lista2)
    print(f"Grade de superposicion {res[0]}, desde la posicion {res[1]}")
    pass


if __name__ == "__main__":
    principal()
