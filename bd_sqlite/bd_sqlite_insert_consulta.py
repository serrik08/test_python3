import sqlite3

conexion = sqlite3.connect("database_example.db")
cursor = conexion.cursor()
#cursor.execute("SELECT * FROM personas")
#cursor.execute("SELECT nombre,edad FROM personas WHERE edad > 30")
cursor.execute("SELECT nombre,apellido1,edad FROM personas ORDER BY edad DESC")
personas = cursor.fetchall()
[print(persona) for persona in personas]

conexion.close()

