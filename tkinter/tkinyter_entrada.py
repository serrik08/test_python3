import tkinter

root = tkinter.Tk()
root.title("Mi programa")

# componente input
entrada = tkinter.Entry(root)
entrada.config(justify="center",show="*")
entrada.pack()

# Componente text, texto largo de varias lineas
entrada_text = tkinter.Text(root)
entrada_text.config(width=20,height=15, font=("Verdana",15),padx=10,pady=10,fg="green",selectbackground="lightgrey")
entrada_text.pack()


def accion_btn():
    print("Hola mundo")

#componente boton
boton = tkinter.Button(root,text="Ejecutar", command=accion_btn)
boton.config(font=("Verdana",15),padx=10,pady=10,fg="green")
boton.pack()


root.mainloop()