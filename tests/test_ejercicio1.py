################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.practica.ejercicio1 import es_par_impar

"""
Tests para la funcion es_par_impar
Donde si es par retorna True y si es Impar retora False
Haciendo casos de pruebas para valores positivos
y negativos
"""


def test_es_par():
    numero = 64
    resultado = es_par_impar(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == True, "el resultado debe ser True"

def test_negativo_impar():
    numero = -89
    resultado = es_par_impar(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == False, "el resultado debe ser False" 

def test_no_es_par():
    numero = 89
    resultado = es_par_impar(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == False, "el resultado debe ser False"


def test_negativo_par():
    numero = -64
    resultado = es_par_impar(numero)
    assert isinstance(resultado, bool), "el resultado debe ser un bool"
    assert resultado == True, "el resultado debe ser True"


   
