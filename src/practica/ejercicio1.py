################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#Precondiciones: Que la entrada sea un numero natural
#----------------------------------------------
#Poscondiciones: Que la salida devuelva un bool


"""
Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo.
(%)
"""
# Reemplazar por las funciones del ejercicio
def es_par_impar(num):
    """
    Esta funcion divide un numero y compara si termina en 0.0 o 0.5
    """
    resto = num / 2
    total = resto
    if ((resto-int(total))==0.0):
        return True
    else:
        return False


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num = int(input("Ingrese numero: "))
    res = es_par_impar(num)
    print(res)
    pass


if __name__ == "__main__":
    principal()
