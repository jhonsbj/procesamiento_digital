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
for i in range(1, largo-1):
    for j in range(1, ancho-1):
        pixel1=(1*imagen[i-1,j-1]+1*imagen[i,j]+1*imagen[i+1,j+1])/3
        pixel2=(1*imagen[i-1,j]+1*imagen[i,j]+1*imagen[i+1,j])/3
        pixel3=(1*imagen[i-1,j+1]+1*imagen[i,j]+1*imagen[i+1,j-1])/3
        pixel4=(imagen[i,j-1]+imagen[i,j]+imagen[i,j+1])/3

        maximo = pixel1

        if (pixel2>maximo):
            maximo = pixel2
        
        if (pixel3>maximo):
            maximo = pixel3

        if(pixel4>maximo):
            maximo = pixel4
        
        if (maximo > 255):
            maximo = 255
        
        temp[i,j] = maximo

plt.title("Imagen Con filtro media")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()