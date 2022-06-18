################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.practica.ejercicio5 import corchetes_balanceados

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_corchetes_balanceados_si():
    cadena = "[]"
    res = corchetes_balanceados(cadena)
    assert res == True, "El resultado tiene que ser True"

def test_corchetes_balanceados_no():
    cadena = "[)"
    res = corchetes_balanceados(cadena)
    assert res == False, "El resultado tiene que ser False"
