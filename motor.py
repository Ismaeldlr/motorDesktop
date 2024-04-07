import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

rotacion_activa = False
angulo_rotacion = 0
imagenes = [] 

def rotar_imagen(direccion):
    global rotacion_activa, angulo_rotacion, imagenes
    while rotacion_activa: 
        angulo_rotacion += 10 if direccion == 'izquierda' else -10 # Aumentamos o disminuimos el ángulo de rotación
        imagen_rotada = imagen.rotate(angulo_rotacion)  # Rotamos la imagen
        imagen_tk = ImageTk.PhotoImage(imagen_rotada) # Creamos un objeto ImageTk con la imagen rotada
        imagenes.append(imagen_tk)  # Guardamos la imagen en la lista
        label_imagen.config(image=imagen_tk) # Actualizamos la imagen en el Label
        time.sleep(0.1)  # Esperamos 0.1 segundos antes de la próxima rotación

def rotar_izquierda(): 
    global rotacion_activa
    rotacion_activa = False  # Detenemos cualquier rotación en curso
    time.sleep(0.1)  # Esperamos un poco para asegurarnos de que la rotación se ha detenido
    rotacion_activa = True  # Iniciamos una nueva rotación
    threading.Thread(target=rotar_imagen, args=('izquierda',)).start()  # Iniciamos la rotación en un hilo separado

def rotar_derecha():
    global rotacion_activa
    rotacion_activa = False  # Detenemos cualquier rotación en curso
    time.sleep(0.1)  # Esperamos un poco para asegurarnos de que la rotación se ha detenido
    rotacion_activa = True  # Iniciamos una nueva rotación
    threading.Thread(target=rotar_imagen, args=('derecha',)).start()  # Iniciamos la rotación en un hilo separado
    
def parar_rotacion():
    global rotacion_activa 
    rotacion_activa = False # Detenemos cualquier rotación en curso

# Creamos una instancia de Tkinter
ventana = tk.Tk()

# Configuramos el título de la ventana
ventana.title("Mi Ventana")

# Configuramos las dimensiones de la ventana
ventana.geometry("700x700")

# Configuramos el color de fondo de la ventana
ventana.configure(bg="white")  # Puedes cambiar "white" al color que desees

# Cargamos la imagen
imagen = Image.open("motor.png") 

# Creamos un objeto ImageTk para mostrar la imagen en Tkinter
imagen_tk = ImageTk.PhotoImage(imagen)

# Creamos un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen_tk, bg="white")  # Configuramos el color de fondo del Label
label_imagen.place(relx=0.5, rely=0.4, anchor=tk.CENTER)  # Centramos la imagen en la ventana

# Creamos los botones
boton1 = tk.Button(ventana, text="Izquierda", command=rotar_izquierda)
boton2 = tk.Button(ventana, text="Parar", command=parar_rotacion)
boton3 = tk.Button(ventana, text="Derecha", command=rotar_derecha)

# Colocamos los botones debajo de la imagen
boton1.place(relx=0.2, rely=0.9, anchor=tk.CENTER)
boton2.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
boton3.place(relx=0.8, rely=0.9, anchor=tk.CENTER)

# Mostramos la ventana
ventana.mainloop()
