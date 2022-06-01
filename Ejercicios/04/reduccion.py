# Función de función aumento
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

imagen=io.imread("/home/lunatico/code/imagendigitial/images/lena_gray.png")
largo = len(imagen)
ancho = len(imagen[0])
largo_p = int(largo/2)
ancho_p = int(ancho/2)
temp = np.zeros((largo_p,ancho_p),dtype=np.uint8)

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

for i in range(0, largo_p):
    i_2 = 2*i
    for j in range(0, ancho_p):
        j_2 = 2*j
        temp[i,j] = imagen[i_2,j_2]

plt.title("Imagen Con filtro media")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()