# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
import math
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("mario.jpg")
# El rano de valores del pixel esta entre 0-255.

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

#Borde por recorrido horizontal
for i in range(0, largo-1):
    for j in range(0, ancho-1):
        nuevo_pixel = abs(imagen[i+1,j]*1 - imagen[i,j]*1)
        #nuevo_pixel = abs(imagen[i+1,j] - imagen[i,j])
        temp[i,j] = nuevo_pixel

plt.title("Detección de borde recorrido horizontal")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

#Borde por recorrido vertical
for i in range(0, largo-1):
    for j in range(0, ancho-1):
        nuevo_pixel = abs(imagen[i,j+1]*1 - imagen[i,j]*1)
        temp[i,j] = nuevo_pixel

plt.title("Detección de borde recorrido vertical")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

temp = np.copy(imagen)
#Borde por valor maximo
for i in range(0, largo-1):
    for j in range(0, ancho-1):

        pixel_der = abs(imagen[i+1,j]*1 - imagen[i,j]*1)
        pixel_arr = abs(imagen[i,j+1]*1 - imagen[i,j]*1)

        maximo = pixel_der

        if (pixel_arr > pixel_der):
            maximo = pixel_arr

        temp[i,j] = maximo

plt.title("Detección de borde maximo")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()