################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.practica.ejercicio3 import super_puestos

"""
Test ejercicio3 funcion super_puestos
En este test enviamos dos listas, y verifica el nivel
de superposicion y la posicion en donde empiezan a colapsar
"""


def test_super_puestos():
    lista1 = ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
    lista2 = ['H', 'o', 'l', 'a']
    res = super_puestos(lista1, lista2)
    assert res[1] == 0, "el resultado debe ser 0"
    assert res[0] == 4, "el resultado debe ser 4"
