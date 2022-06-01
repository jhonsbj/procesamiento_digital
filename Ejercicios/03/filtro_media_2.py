# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("adapgaussian.jpg")

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()
nuevo_pixel = 0

for i in range(1, largo-1):
    for j in range(1, ancho-1):
        media = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                media = media + imagen[i+x,j+y]*1/9

        temp[i,j] = media

plt.title("Imagen Con filtro media primera aplicacion")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()
'''
for i in range(1, largo-1):
    for j in range(1, ancho-1):
        media = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                media = media + temp[i+x,j+y]*1/9
    
        if (media < 0 or media>255):
            print(media)
        temp[i,j] = media
plt.title("Imagen Con filtro media segunda aplicacion")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

for i in range(1, largo-1):
    for j in range(1, ancho-1):
        media = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                media = media + temp[i+x,j+y]*1/9
    
        if (media < 0 or media>255):
            print(media)
        temp[i,j] = media
plt.title("Imagen Con filtro media tercera aplicacion")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()

for i in range(1, largo-1):
    for j in range(1, ancho-1):
        media = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                media = media + temp[i+x,j+y]*1/9
    
        if (media < 0 or media>255):
            print(media)
        temp[i,j] = media
plt.title("Imagen Con filtro media cuarta aplicacion")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()
'''