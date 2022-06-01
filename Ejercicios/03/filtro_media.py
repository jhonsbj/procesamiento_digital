# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("mario.jpg")

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()
nuevo_pixel = 0

#Cuenta los colores de la imagen
for i in range(1, largo):
    for j in range(1, ancho):
        pixel1=imagen[i-1,j-1]*1/4
        pixel2=imagen[i-1,j]*1/4
        pixel3=imagen[i,j-1]*1/4
        pixel_actual=imagen[i,j]*1/4
        nuevo_pixel = pixel1+pixel2+pixel3+pixel_actual
        #print (nuevo_pixel)
        temp[i,j] = nuevo_pixel

plt.title("Imagen Con filtro media")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()