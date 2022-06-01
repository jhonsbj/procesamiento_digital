# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
import math
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("lena_gray.png")
# El rano de valores del pixel esta entre 0-255.

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

f1 = [[-1,0,1],
[-1,0,2],
[-1,0,1]]

f2 = [[-1,-2,-1],
[0,0,0],
[1,2,1]]

for i in range(1, largo-1):
    for j in range(1, ancho-1):
       
        color = 0
        m = (imagen[i-1,j+1] + 2*imagen[i,j+1] + imagen[i+1,j+1]) - (imagen[i-1,j-1] + 2*imagen[i,j-1] + imagen[i+1,j-1])
        n = (imagen[i-1,j+1] + 2*imagen[i,j+1] + imagen[i+1,j+1]) - (imagen[i-1,j-1] + 2*imagen[i-1,j] + imagen[i-1,j+1])

        #m = (1*imagen[i-1,j+1] + 1*imagen[i,j+1] + 1*imagen[i+1,j+1]) - (1*imagen[i-1,j-1] + 1*imagen[i,j-1] + 1*imagen[i+1,j-1])
        #n = (1*imagen[i-1,j+1] + 1*imagen[i,j+1] + 1*imagen[i+1,j+1]) - (1*imagen[i-1,j-1] + 1*imagen[i-1,j] + 1*imagen[i-1,j+1])
        m = abs(m)
        n = abs(n)
        color = math.sqrt(m**2+n**2)

        if (color>255):
            color=255
                
        temp[i,j] = color


plt.title("Detección de borde Sobel")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()


