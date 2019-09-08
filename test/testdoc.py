# Doctest - generar pruebas dentro de la documentacion

def sumar(numero1,numero2):
    """
    Esto es la documentacion de la funcion
    Recibe dos numeros como parametros y devuelve su suma
    
    >>> sumar(4,3)
    7
    >>> sumar(5,4)
    1
    >>> sumar(10,1)
    11

    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()