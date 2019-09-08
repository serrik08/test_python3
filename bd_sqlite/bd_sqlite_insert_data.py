import sqlite3

conexion = sqlite3.connect("database_example.db")
cursor = conexion.cursor()
#cursor.execute("INSERT INTO personas values('Antonio','Perez','Lopez',35)")

lista_personas = [
    ('Pedro','Rodrigues','Obrador',25),
    ('Ana','Gomez','Fuentes',20),
    ('Lucia','Cardenas','Garcia',31)
]
cursor.executemany("INSERT INTO personas VALUES (?,?,?,?)", lista_personas)
conexion.commit()

conexion.close()

