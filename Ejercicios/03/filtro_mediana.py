# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("lena_ruido.png")

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

for i in range(1, largo-1):
    for j in range(1, ancho-1):
        mediana = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                mediana.append(imagen[i+x,j+y])

        mediana.sort()

        temp[i,j] = mediana[4]

plt.title("Imagen Con filtro mediana")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

