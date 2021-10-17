

# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import filedialog # NICO: Para abrir archivos con el explorador
from tkinter import messagebox
# Define la ventana principal de la aplicación

raiz = Tk()   # Raiz es la ventana RAIZ

# Define las dimensiones de la ventana, que se ubicará en 
# el centro de la pantalla. Si se omite esta línea la
# ventana se adaptará a los widgets que se coloquen en
# ella. 

raiz.geometry('600x400') # anchura x altura

# Asigna un color de fondo a la ventana. EN HEXA

raiz['bg'] = '#E1F9FF'
# Asigna un título a la ventana

raiz.title('MeterPeter´s Gestor')



raiz.iconbitmap("icon.ico")


lbl=Label(raiz, text="Selecione primero un archivo de texto")
txt = Entry(raiz,width=10)

ruta = "Nada"

def abrirArchivo():
    archivo =filedialog.askopenfilename(title="Elegi GIL",filetypes=(("Archivos de Texto", "*.txt"),))
    print(archivo)
    ruta="Ruta: "+archivo
    print(ruta)
    lbl.configure(text=ruta)
    # NICO: Aca se puede poner las lineas que convierten el texto!!!
    # NICO: Abrir el archivo y guardarlo tambien supongo

    
def ConvertirArchivo():

    messagebox.showinfo(message="Ahora metele a programar como convertir el texto (abrir el archivo que ya tenes la ruta) y despues guardar en algun lugar con el explorador ;)", title="MUY BIEN")



Button(raiz,text="Abrir archivo",command=abrirArchivo).pack()
lbl.pack()
Button(raiz,text="Convertir Archivo",command=ConvertirArchivo).pack()
# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón

ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)








# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de 
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.
raiz.mainloop()