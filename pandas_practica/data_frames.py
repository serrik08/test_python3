import pandas as pd
import webbrowser

website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'

#webbrowser.open(website)

# dataframe_nba = pd.read_clipboard()

# #Muestra las columnas
# dataframe_nba.columns
# #accede a datos de columna
# dataframe_nba['1950']
# # Fila
# dataframe_nba.loc[5]
# # Muestra el numero de elementos, desde el inicio
# dataframe_nba.head(3)
# # Muestra los ultimos elementos
# dataframe_nba.tail(2)

asignaturas = ['mate','fisica','quimica','historia']
notas = [3,2,5,9]
diccionario = { 'Asignaturas': asignaturas,'Notas':notas}
print(diccionario)

dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)