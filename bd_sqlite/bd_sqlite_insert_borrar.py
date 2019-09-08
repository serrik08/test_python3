import sqlite3

conexion = sqlite3.connect("database_example.db")
cursor = conexion.cursor()
cursor.execute("DELETE FROM personas WHERE nombre = 'Lucia'")
conexion.commit()
conexion.close()

