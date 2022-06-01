# Función Filtro de Relieve de Imagen
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
import math
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("edificio.jpg")
# El rano de valores del pixel esta entre 0-255.

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()
q = 127 # (256-1) /2

#q = 63 # (128-1) /2

#Borde por recorrido horizontal
for i in range(0, largo-1):
    for j in range(0, ancho-1):
        nuevo_pixel = q +  abs(imagen[i+1,j]*1) - abs(imagen[i,j]*1)

        if (nuevo_pixel > 255):
            nuevo_pixel=255

        temp[i,j] = nuevo_pixel

plt.title("Filtro de Relieve de Imagen recorrido horizontal")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

#Borde por recorrido vertical
for i in range(0, largo-1):
    for j in range(0, ancho-1):
        nuevo_pixel = q + abs(imagen[i,j+1]*1) - abs(imagen[i,j]*1)

        if (nuevo_pixel > 255):
            nuevo_pixel=255


        temp[i,j] = nuevo_pixel

plt.title("Filtro de Relieve de Imagen recorrido vertical")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

m = [[-1,-1,-1],[0,0,0],[1,1,1]]
temp = np.copy(imagen)

#Borde por valor maximo
for i in range(1, largo-1):
    for j in range(1, ancho-1):
        color = 0
        for a in [-1,0,1]:
            for b in [-1,0,1]:
                color = color + m[a+1][b+1] * abs(imagen[i+a,j+b]*1) 
                
        color = q + color
        if (color > 255):
            color=255

        if (color < 0):
            color = 0

        temp[i,j] = color

plt.title("Filtro de Relieve de Imagen matriz")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()