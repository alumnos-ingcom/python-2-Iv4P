################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.practica.ejercicio2 import estadisticas

"""
Test del ejercicio2, estadisticas, este test le envia una lista
a la funcion estadistica y nos devuelve el maximo, minimo y el promedio 
en forma de tupla
"""


def test_estadisticas():
    lista = [14, 65, 23]
    res = estadisticas(lista)
    assert isinstance(res, tuple), "El resultado debe ser una tuple"
    assert res[0] == 65, "El resultado tiene que ser 65"
    assert res[1] == 14, "El resultado tiene que ser 14"
    assert res[-1] == 34, "El promedio debe ser 34"