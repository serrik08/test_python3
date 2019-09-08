

texto = "Hola mi nombre es sergio"

import re

#res = re.search("nombre",texto)
#res = re.search("sergio$",texto)
res = re.search("^Hola",texto)

print("Cadena encontrada" if res else "Cadena no encontrada")

texto2 = "el coche de luis es rojo\
    el coche de maria es rojo\
        y el choche de fernando es azul"

print(re.findall("coche.*rojo",texto2))

texto3 = "el coche de luis es rojo"

print(re.split("\s",texto3))


texto4 = "la silla es morada"

print(re.sub("morada","blanca",texto4))
