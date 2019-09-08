import pandas as pd
import numpy as np

#reemplazar valores en series
serie1 = pd.Series([1,2,3,4,5],index=list('abcde'))
print(serie1)

serie2 = serie1.replace(1,6)
print(serie2)

serie3 = serie2.replace({2:8,3:9})
print(serie3)

#renombrar indices
lista_valores = np.arange(9).reshape(3,3)
print(lista_valores)

lista_indices = list('abc')

dataframe1 = pd.DataFrame(lista_valores,index=lista_indices)
print(dataframe1)

nuevos_indices =  dataframe1.index.map(str.upper)

dataframe1.index = nuevos_indices
print(dataframe1)

dataframe1 = dataframe1.rename(index=str.lower)
print(dataframe1)

nuevos_indices = {'a':'f','b':'g'}

dataframe1 = dataframe1.rename(index=nuevos_indices)
print(dataframe1)