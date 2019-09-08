# -*- coding: utf-8 -*-
try:
    numero1 = 5
    numero2 = 0
    division = numero1/numero2
    print(division)
except ZeroDivisionError:
    print("Error al dividir por 0")
except:
    print("Ha ocurrido un error")
else:
    print("La division funciono correctamente")
finally:
    print("Esta prueba del try se ha acabado")
