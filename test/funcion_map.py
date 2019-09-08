#map

def multiplicar(numero):
    return numero*2

print(multiplicar(2))

numeros = [2,4,6]

mapeo = map(multiplicar,numeros)

resultado = list(mapeo)

print(resultado)


lista_resultado = list(map(lambda numero: numero*3, numeros))
print(lista_resultado)