#Aarón Grillo Cruz

from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # Para el mensaje de confirmación al salir

# Tasa de conversión fija 
TASA_CONVERSION = 517.40

def calcular(*args):
    """Función para convertir de USD a CRC."""
    try:
        value = float(Dolares.get())
        Colones.set(f"{TASA_CONVERSION * value:,.2f} CRC")  
    except ValueError:
        Colones.set("ERROR: Entrada no válida")

def limpiar():
    """Función para limpiar los campos de entrada y salida."""
    Dolares.set("")
    Colones.set("")

def confirmar_cierre():
    """Función para confirmar el cierre de la aplicación."""
    if messagebox.askokcancel("Salir", "¿Seguro que deseas salir?"):
        ventana.destroy()

# Crear ventana
ventana = Tk()
ventana.title("Conversor USD a CRC")
ventana.geometry("350x150")  # Tamaño de la ventana
ventana.resizable(False, False)  # No redimensionar

# Márgenes de la ventana
mainframe = ttk.Frame(ventana, padding="10 5 10 5")
mainframe.grid(row=0, column=0, sticky=(N, W, E, S))

# Variables para la conversión
Dolares = StringVar()
Colones = StringVar()

# Campo de entrada para los dólares
Dolares_entry = Entry(mainframe, width=10, textvariable=Dolares)
Dolares_entry.grid(row=0, column=2)
Label(mainframe, text="Dólares").grid(row=0, column=3, sticky=W)


Label(mainframe, text="Es equivalente a:").grid(row=1, column=1, sticky=E)
Label(mainframe, textvariable=Colones).grid(row=1, column=2, sticky=W)
Label(mainframe, text="Colones").grid(row=1, column=3, sticky=W)

# Botón de conversión
Button(mainframe, text="Convertir", command=calcular).grid(row=2, column=2, sticky=W)

# Botón de limpiar
Button(mainframe, text="Limpiar", command=limpiar).grid(row=2, column=3, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


Dolares_entry.focus()
ventana.bind("<Return>", calcular)


ventana.protocol("WM_DELETE_WINDOW", confirmar_cierre)
ventana.mainloop()