# Función de función media
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

imagen=io.imread("W9K501.jpg")

temp = np.copy(imagen)
largo = len(temp)
ancho = len(temp[0])

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()
nuevo_pixel = 0
perfilado = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
for i in range(1, largo-1):
    for j in range(1, ancho-1):
        color = 0
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                color = color + perfilado[x+1][y+1] * (imagen[i+x,j+y]*1) 

        if (color < 0):
            color = 0

        if(color > 255):
            color = 255

        temp[i,j] = color

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