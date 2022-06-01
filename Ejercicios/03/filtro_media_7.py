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
nuevo_pixel = 0

#Cuenta los colores de la imagen
for i in range(0, largo):
    for j in range(0, ancho):
        media = 0
        pixeles = 0
        for x in [-4,-3,-2,-1,0,1,2,3,4]:
            for y in [-4,-3,-2,-1,0,1,2,3,4]:
                try:
                    media = media + imagen[i+x,j+x]*1
                    pixeles = pixeles+1
                except:
                    continue
        
        temp[i,j] = media/pixeles

plt.title("Imagen Con filtro media")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()