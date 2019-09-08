import pickle

list_colors = ["rojo","amarillo","verde"]

fichero = open("file_colors.pckl","wb")

pickle.dump(list_colors,fichero)

fichero.close()


fichero = open("file_colors.pckl","rb")

lista_leida = pickle.load(fichero)

print(lista_leida)

fichero = open("file_colors.pckl", "rb")
lista_leida = pickle.load(fichero)
print(lista_leida)