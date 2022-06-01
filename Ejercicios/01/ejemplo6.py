
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

image=io.imread("lena_gray.png")/255.0 # imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

temp = np.copy(image)
nivel = 0.5

print("- Dimensiones de la imagen:")

print(image.shape)
plt.imshow(image,vmin=0,vmax=1)
plt.show()

for i in range(0,511):
    for j in range(0,511):
        temp[i,j]=temp[i,j]+nivel

plt.imshow(temp,vmin=0,vmax=1)
plt.show()

for i in range(0,511):
    for j in range(0,511):
        temp[i,j]=temp[i,j]-nivel

plt.imshow(temp,vmin=0,vmax=1)
plt.show()