

# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import filedialog # NICO: Para abrir archivos con el explorador

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

raiz.resizable(0,0)

raiz.iconbitmap("icon.ico")
ruta = ""

lbl1 = Label(raiz, text=ruta)
lbl = Label(raiz, text="RUTA").pack
lbl2as = Label(raiz, text="Hello", font=("Arial Bold", 50))

def abrirArchivo():
    archivo =filedialog.askopenfilename(title="Elegi GIL",filetypes=(("Archivos de Texto", "*.txt"),))
    print(archivo)
    ruta=archivo
    # NICO: Aca se puede poner las lineas que convierten el texto!!!
    # NICO: Abrir el archivo y guardarlo tambien supongo
    

Button(raiz,text="Abrir archivo",command=abrirArchivo).pack()










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