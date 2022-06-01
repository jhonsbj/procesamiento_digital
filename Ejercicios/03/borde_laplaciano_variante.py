# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
import math
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("ejemplo_bn.jpg")
# El rano de valores del pixel esta entre 0-255.

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

#Borde por recorrido horizontal
for i in range(1, largo-1):
    for j in range(1, ancho-1):
        pixel_esq_izq_arr = imagen[i-1,j-1]*1
        pixel_esq_der_arr = imagen[i+1,j-1]*1
        pixel_esq_izq_aba = imagen[i-1,j+1]*1
        pixel_esq_der_aba = imagen[i+1,j+1]*1
        pixel_izquierda = imagen[i-1,j]*1
        pixel_arriba = imagen[i,j-1]*1
        pixel_derecha = imagen[i+1,j]*1
        pixel_abajo = imagen[i,j+1]*1
        pixel_actual = imagen[i,j]*1

        color = -1*pixel_esq_izq_arr-pixel_arriba-pixel_esq_der_arr-pixel_izquierda+8*pixel_actual-pixel_derecha-pixel_esq_izq_aba-pixel_abajo-pixel_esq_der_aba  
        color = abs(color)

        if (color > 255):
            color=255

        temp[i,j] = color

plt.title("Detección de borde gradiente")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()
