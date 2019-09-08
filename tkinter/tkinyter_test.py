import tkinter

root = tkinter.Tk()
root.title("Mi programa")

#Creando componente frame
frame = tkinter.Frame(root)
frame.config(bg="blue", width=500,height=300)
frame.pack()

#label
texto = "hola mundo"
etiqueta = tkinter.Label(root,text=texto)
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
etiqueta.pack( )

root.mainloop()