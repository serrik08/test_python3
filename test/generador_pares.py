# Funcion generadora de pares

def pares(maximo):
    for numero in range(maximo):
        if (numero % 2 == 0):
            yield numero


maximo = 13
for numero in pares(maximo):
    print(numero)