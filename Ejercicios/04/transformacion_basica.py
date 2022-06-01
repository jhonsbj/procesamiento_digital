# Transformación básica
# importamos el modulo pyplot, y lo llamamos plt
#import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
#plt.rcParams['image.cmap'] = 'gray'

#from skimage import io

imagen=cv.imread("lena_gray.png")

temp_180 = np.copy(imagen)
mx = len(temp_180)-1
my = len(temp_180[0])-1

temp_90 = []

plt.title("Imagen original")
plt.imshow(imagen,vmin=0,vmax=255)
plt.show()
'''
#Cuenta los colores de la imagen
for x in range(0,mx):
    for y in range(0,my):
        temp_180[x,y]=imagen[mx-x,my-y]

plt.title("Rotación 180")
plt.imshow(temp_180,vmin=0,vmax=255)
plt.show()

# Crear la nueva matriz
for x in range(0,my):
    fila = []
    for y in range(0,mx):
        fila.append(0)
    
    temp_90.append(fila)


#Rota la imagen 90 grados
for x in range (0,my):
    for y in range(0,mx):
        temp_90[x][y]=imagen[y,my-x]

plt.title("Rotación 90 grados")
plt.imshow(temp_90,vmin=0,vmax=255)
plt.show()

for x in range (0,my):
    for y in range(0,mx):
        temp_90[x][y]=imagen[mx-y,x]

plt.title("Rotacion 270 grados")
plt.imshow(temp_90,vmin=0,vmax=255)
plt.show()
'''
for x in range (0,mx):
    for y in range(0,my):
        temp_180[x,y]=imagen[mx-x,y]

plt.title("Espejo vertical")
plt.imshow(temp_180,vmin=0,vmax=255)
plt.show()

for x in range (0,mx):
    for y in range(0,my):
        temp_180[x,y]=imagen[x,my-y]

plt.title("Espejo horizontal")
plt.imshow(temp_180,vmin=0,vmax=255)
plt.show()
