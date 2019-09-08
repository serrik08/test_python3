
import pandas as pd

serie1 = pd.Series([3,5,7])
print(serie1)
print(serie1[2])

# creando indices
asignaturas = ['mate','fisica','literatura','historia']
notas = [8,9,7,5]
serie_notas_daniel = pd.Series(notas,index=asignaturas)

print(serie_notas_daniel['fisica'])
print(serie_notas_daniel[serie_notas_daniel >= 8])

serie_notas_daniel.name = "notas de Daniel"
serie_notas_daniel.index.name = "Asignaturas"
print(serie_notas_daniel)

diccionario = serie_notas_daniel.to_dict()
print(diccionario)

serie = pd.Series(diccionario)
print(serie)

notas_ana = [6,7,5,9]
serie_notas_ana = pd.Series(notas_ana,index=asignaturas)
print(serie_notas_ana)

serie_promedio = (serie_notas_daniel + serie_notas_ana) /2
print(serie_promedio)