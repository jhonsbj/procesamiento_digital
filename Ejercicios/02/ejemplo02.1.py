# Negativo de una imagen
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

image=io.imread("lena_gray.png")
# El rano de valores del pixel esta entre 0-255.

temp = np.copy(image)

plt.title("Imagen original")
plt.imshow(image,vmin=0,vmax=255)
plt.show()

for i in range(0,len(temp)):
    for j in range(0,len(temp[0])):
        temp[i,j]=255-temp[i,j]

plt.title("Negativo de la imagen")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()