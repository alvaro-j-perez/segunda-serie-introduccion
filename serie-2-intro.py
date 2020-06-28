import tkinter as tk
import math

def funcionUno():
    a=int(inputUno.get())
    b=int(inputDos.get())
    c=int(inputTres.get())
    d=int(inputCuatro.get())    
    e=int(inputCinco.get())
    numeros = [a,b,c,d,e]

    ordenados = sorted(numeros)

    return var.set(ordenados)

def funcionDos():
    datos=int(inputCinco.get())
    result = int()
    contador = 1
    for result in range(datos):
        contador += 1
        result =int(inputUno.get())*int(inputUno.get())
        return var.set(result + contador)
    

def funcionTres():
    suma=int(inputUno.get())+int(inputUno.get())
    return var.set(suma)
def funcionCuatro():
    suma=int(inputUno.get())+int(inputUno.get())
    return var.set(suma)
def funcionCinco():
    suma=int(inputUno.get())+int(inputUno.get())
    return var.set(suma)

ventanaExamen = tk.Tk()
ventanaExamen.title("Examen Final")

ventanaExamen.geometry("600x600")

ventanaExamen.resizable(False, False)
var=tk.StringVar()


labelUno=tk.Label(ventanaExamen, text="Numero 1", bg="DimGray", fg="blue4")
labelUno.pack(padx=5, pady=4, ipady=5, fill=tk.X)


inputUno=tk.Entry(ventanaExamen)
inputUno.pack(fill=tk.X,padx=5, pady=5, ipady=5)




labelDos=tk.Label(ventanaExamen, text="Numero 2", bg="DimGray", fg="blue4")
labelDos.pack(padx=5, pady=6, ipady=5, fill=tk.X)


inputDos=tk.Entry(ventanaExamen)
inputDos.pack(fill=tk.X,padx=7, pady=5, ipady=5)



labelTres=tk.Label(ventanaExamen, text="Numero 3", bg="DimGray", fg="blue4")
labelTres.pack(padx=5, pady=8, ipady=5, fill=tk.X)


inputTres=tk.Entry(ventanaExamen)
inputTres.pack(fill=tk.X,padx=9, pady=5, ipady=5)


labelCuatro=tk.Label(ventanaExamen, text="Numero 4", bg="DimGray", fg="blue4")
labelCuatro.pack(padx=5, pady=10, ipady=5, fill=tk.X)


inputCuatro=tk.Entry(ventanaExamen)
inputCuatro.pack(fill=tk.X,padx=11, pady=5, ipady=5)


labelCinco=tk.Label(ventanaExamen, text="Numero 5", bg="DimGray", fg="blue4")
labelCinco.pack(padx=5, pady=12, ipady=5, fill=tk.X)


inputCinco=tk.Entry(ventanaExamen)
inputCinco.pack(fill=tk.X,padx=13, pady=5, ipady=5)





resultado=tk.Label(ventanaExamen, bg="dark salmon", textvariable=var, padx=14, pady=5, width=100)
resultado.pack()

btnfuncionUno=tk.Button(ventanaExamen, text="Funcion 1", fg="blue", command=funcionUno).place(x=10,y=500)

btnfuncionDos=tk.Button(ventanaExamen, text="Funcion 2", fg="blue", command=funcionDos).place(x=90,y=500)

btnfuncionTres=tk.Button(ventanaExamen, text="Sin Implementar", fg="blue", command=funcionTres).place(x=180,y=500)

btnfuncionCuatro=tk.Button(ventanaExamen, text="Sin Implementar", fg="blue", command=funcionCuatro).place(x=300,y=500)

btnfuncionCinco=tk.Button(ventanaExamen, text="Sin Implementar", fg="blue", command=funcionCinco).place(x=410,y=500)

ventanaExamen.mainloop()