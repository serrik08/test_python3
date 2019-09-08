# Dockstring - cadenas para documentacion

class Saludo():
    """
    Esta clase tendra dos funciones saludos y adios
    ambas funciones recibiran como parametro un nombre
    """

    def buenos_dias(self,nombre):    
        """
        Esta funcion recibira como parametro una cadenas
        con el nombre, e imprimira por pantalla un saludo con el nombre concatenado
        """
        print("buenos dias {}".format(nombre))
    
    def adios(self,nombre):    
        """
        Esta funcion recibira como parametro una cadenas
        con el nombre, e imprimira por pantalla una despedida con el nombre concatenado
        """
        print("buenos dias {}".format(nombre))

saludo = Saludo()
saludo.buenos_dias("Ana")

help(Saludo)
