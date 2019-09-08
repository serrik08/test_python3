import tkinter
from tkinter import messagebox
from tkinter import filedialog

root = tkinter.Tk()
root.title("Mi programa")

# componente radiobutton
def seleccionar():
    print("La opcion seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(root,text="opcion 1",variable=opcion,value=1,command=seleccionar)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(root,text="opcion 2",variable=opcion,value=2,command=seleccionar)
radiobutton2.pack()

radiobutton3 = tkinter.Radiobutton(root,text="opcion 3",variable=opcion,value=3,command=seleccionar)
radiobutton3.pack()

# componente checkout
def verificar():
    valor =opcion_check1.get()
    if valor==1:
        print("el check esta activo")
    else:
        print("el check esta inactivo")

opcion_check1 = tkinter.IntVar()

chekc1 = tkinter.Checkbutton(root,text="opcion 1",variable=opcion_check1,onvalue=1,offvalue=0,command=verificar)
chekc1.pack()

# Componente messsagebox
def avisar():
    tkinter.messagebox.showinfo("Titulo aviso","Mensade con la informacion")

boton1 = tkinter.Button(root,text="Pulsar para aviso", command=avisar)
boton1.pack()

# Ventana de confirmacion
def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo pregunta","¿pregunta?")
    print("el resultado es : {}".format(resultado))

boton2 = tkinter.Button(root,text="Pulsar para preguntar", command=preguntar)
boton2.pack()

# Ventana abrir fichero
def abrir_fichero():
    resultado = filedialog.askopenfilename(title="Abrir fichero")
    print("el resultado es : {}".format(resultado))

boton3 = tkinter.Button(root,text="Pulsar para empezar", command=abrir_fichero)
boton3.pack()


root.mainloop()