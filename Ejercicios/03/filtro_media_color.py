# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises

from skimage import io

imagen=io.imread("lena.png")

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()

#Cuenta los colores de la imagen
for i in range(0, largo):
    for j in range(0, ancho):
        media_1 = 0
        media_2 = 0
        media_3 = 0
        pixeles = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                try:
                    media_1 = media_1 + imagen[i+x,j+x,0]*1
                    media_2 = media_2 + imagen[i+x,j+x,1]*1
                    media_3 = media_3 + imagen[i+x,j+x,2]*1
                    pixeles = pixeles+1
                except:
                    continue
        
        temp[i,j,0] = media_1/pixeles
        temp[i,j,1] = media_2/pixeles
        temp[i,j,2] = media_3/pixeles

plt.title("Imagen Con filtro media")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()