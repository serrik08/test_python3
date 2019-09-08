# Filter

def positivo(numero):
    if numero > 0:
        return True
    else:
        return False

numeros = (4,-6,3,78,-10,-4,23)

filtro = filter(positivo,numeros)

resultado = list(filtro)
print(resultado)