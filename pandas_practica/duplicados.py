import pandas as pd
import numpy as np

lista_valores = [[1,2],[1,2],[5,6],[5,8]]
print(lista_valores)

lista_indices = ['m','n','o','p']
print(lista_indices)

lista_columnas = ['valor1','valor2']
print(lista_columnas)

dataframe1 = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)
print(dataframe1)

dataframe2 = dataframe1.drop_duplicates()
print(dataframe2)

dataframe3 = dataframe2.drop_duplicates(['valor1'])
print(dataframe3)

dataframe4 = dataframe2.drop_duplicates(['valor1'], keep='last')
print(dataframe4)