################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
El cifrado César o cifrado de rotación usa una encriptación de sustitución simple.
Esto significa que cada caracter se sustituye por otro caracter de acuerdo con un sistema especifico.
Implementar una funcion que codifique un texto rotandolo una cantidad de posiciones ajustable.
Implementar la funcion que decodifique el texto rotado una cantidad de posiciones ajustable.
"""

def cifrado(cadena, n):
    """
    Esta funcion se encarga de mover n posiciones el caracter 
    modificado al codigo ASCII 
    ejemplo A en ASCII es 65, + 5 (70) seria F 
    """
    cadena = cadena.lower()
    total = ""
    for i in cadena:
        if ord(i) >96 and ord(i) <123:
            if ord(i)+n > 122:
                total = total + chr(ord(i)-26+n)
            else:
                total = total + chr(ord(i)+n)
    return total

def descifrado(cadena, n):
    """
    Esta funcion se encarga de mover n posiciones el caracter 
    modificado al codigo ASCII ya convertido 
    ejemplo Si es F en ASCII es 70, - 5 (65) seria A
    """
    total = ""
    for i in cadena:
        if ord(i) >96 and ord(i) <123:
            if ord(i)-n < 97:
                total = total + chr(ord(i)+26-n)
            else:
                total = total + chr(ord(i)-n)
    return total

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese la palabra a encriptar: ")
    n = int(input("Ingrese numero por el cual encriptar: "))
    res = cifrado(cadena, n)
    res2 = descifrado(res, n)
    print(res)
    print(res2)

if __name__ == "__main__":
    principal()
