from datetime import datetime

fecha_hora = datetime.now()
print(fecha_hora)
year = fecha_hora.year
month = fecha_hora.month
day = fecha_hora.day
hora = fecha_hora.hour
minuto = fecha_hora.minute
segundo = fecha_hora.second
microsecond = fecha_hora.microsecond

print("La hora es {}:{}:{}".format(hora,minuto,segundo))