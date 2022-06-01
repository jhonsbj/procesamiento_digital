# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("lena_gray.png")

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

pond = 8

for i in range(1, largo-1):
    for j in range(1, ancho-1):
        media = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if (x==0 and y==0):
                    media = media + pond*imagen[i+x,j+y]*1/(8+pond)
                    continue

                media = media + imagen[i+x,j+y]*1/(8+pond)

        temp[i,j] = media

plt.title("Imagen Con filtro media")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()