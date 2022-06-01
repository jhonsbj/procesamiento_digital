# Función Senoidal

# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
import math

#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

image=io.imread("lena_gray.png") # imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

temp = np.copy(image)

plt.title("Imagen original")
plt.imshow(image,vmin=0,vmax=255)
plt.show()


for i in range(0,len(temp)):
    for j in range(0,len(temp[0])):
        z = temp[i,j]
        z2 = 255*math.sin((3.14*z)/(2*255))
        temp[i,j]=z2

plt.title("Imagen aclarada")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

