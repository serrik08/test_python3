import sqlite3

conexion = sqlite3.connect("database_example.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE personas (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")
conexion.commit()

conexion.close()

