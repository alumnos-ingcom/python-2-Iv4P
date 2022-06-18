################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento es la suma de los dos anteriores. 
En la misma, los dos primeros términos son 1.
(En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci.
Siendo este número un entero positivo mayor a 2
"""
# Reemplazar por las funciones del ejercicio
def fibonacci(cant):
    """
    Esta funcion retorna el numero de fibonacci 
    correspondiente a la posicion pedida 
    por el usuario
    """
    num1 = 0
    num2 = 1
    total = 0
    i = 1
    while i <= cant:
        i = i + 1 
        num1 = num2 
        num2 = total
        total = num1 + num2
    return total

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cant = int(input("Ingrese el termino de fibonacci: "))
    res = fibonacci(cant)
    print(f"El numero {cant} de fibonacci es {res}")


if __name__ == "__main__":
    principal()
