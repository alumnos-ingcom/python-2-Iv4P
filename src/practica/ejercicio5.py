################
# Iván Piñero - @Iv4P
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Enunciado del ejercicio
"""
# Reemplazar por las funciones del ejercicio
def corchetes_balanceados(cadena):
    """
    Esta funcion guarda los simbolos cuando aparecen
    Luego verifica las posiciones de la cadena
    y si en la posicion de la cadena hay un simbolo, se guarda en la nueva cadena
    sino si la longitud de la nueva cadena es 0 o la posicion de la cadena es distinta al diccionario 
    los simbolos, saca el simbolo de la nueva cadena y retorna False
    Si la longitud de la nueva cadena es 0 retorna True
    """
    cad = []
    simbolos = {'{': '}', '(': ')', '[': ']'}
    for i in cadena:
        if i in simbolos:
            cad.append(i)
        elif len(cad) == 0 or i != simbolos[cad.pop()]:
            return False    
    return len(cad) == 0

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese la cadena a verificar: ")
    res = corchetes_balanceados(cadena)
    print(f"Los simbolos de la cadena estan abiertos y cerrados correctamente? {res}")


if __name__ == "__main__":
    principal()
