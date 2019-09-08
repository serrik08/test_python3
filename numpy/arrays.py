# Creando array

import numpy as np

np.zeros(4)
print(np.zeros(4))

np.ones(4)
print(np.ones(4))

np.arange(4)
print(np.arange(4))

np.arange(10)
print(np.arange(10))

np.arange(2,20,3)
print(np.arange(2,20,3))

lista1 = [1,2,3,4]
array1 = np.array(lista1)
print(array1)

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)
print(array_doble)

print(array_doble.shape)

print(array_doble.dtype)