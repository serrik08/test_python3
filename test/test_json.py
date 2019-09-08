# JSON
# Converti datos de un dict a json

producto1 = { "nombre":"silla", "color":"negro", "precio":30}
import json
json_obj = json.dumps(producto1)
print(json_obj)
dict_obj = json.loads(json_obj)
print(dict_obj)