import sqlite3

conexion = sqlite3.connect("database_example.db")
cursor = conexion.cursor()
cursor.execute("UPDATE personas SET edad=29 WHERE nombre = 'Ana'")
conexion.commit()
conexion.close()

