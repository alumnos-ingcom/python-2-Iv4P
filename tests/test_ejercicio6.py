################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.practica.ejercicio6 import cifrado, descifrado

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_cifrado():
    cadena = "HoLa"
    n = 4
    res = cifrado(cadena, n)
    assert res == "lspe", "El resultado tiene que ser LsPe"

def test_descifrado():
    cadena = "lspe"
    n = 4
    res = descifrado(cadena, n)
    assert res == "hola", "El resultado tiene que ser HoLa"

