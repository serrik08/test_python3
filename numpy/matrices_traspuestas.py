
import numpy as np

array = np.arange(15).reshape((3,5))
print(array)

print(array[1][3])

array_tras = array.T
print(array_tras)

#entrada y salida de arrays
array2 = np.arange(5)
print(array2)
np.save('array1s',array2)
print(np.load('array1s.npy'))

array3 = np.arange(8)

np.savez('arrays',x=array2,y=array3)
array_recuperado = np.load('arrays.npz')
print(array_recuperado['x'])

np.savetxt('mificheroarray.txt',array3,delimiter=',')
print(np.loadtxt('mificheroarray.txt',delimiter=','))