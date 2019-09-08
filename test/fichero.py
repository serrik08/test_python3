# Abrir fichero
fichero = open("file.txt","rt")
datos_fichero = fichero.read()
print(datos_fichero)

# Crear fichero
fichero2 = open("new_file.txt","wt")
texto_del_fichero = "hola, esta es la\n\
    linea que vamos a grabar\n\
        del fichero"
fichero2.write(texto_del_fichero)
fichero2.close()

# Añadir fichero
fichero3 = open("file.txt","at")
cadena_para_incluir = "\nEsta es la terce linea"
fichero3.write(cadena_para_incluir)
fichero3.close()

# Borrar fichero
import os
os.remove("borrar.txt")