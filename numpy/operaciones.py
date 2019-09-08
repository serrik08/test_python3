# Operaciones con arrays

import numpy as np

array1 = np.array([1,2,3,4,5])
#print(array1)

#print(array1 + 4)

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)
print(array_doble)

print (array_doble ** 2)

array = np.arange(0,11)
print(array)
print(array[0:3])
print(array[2:5])

array_copia = array.copy()
array_copia[:3] = 20
print(array_copia)

#dimensiones
array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(array2)

print(array2[2][1])