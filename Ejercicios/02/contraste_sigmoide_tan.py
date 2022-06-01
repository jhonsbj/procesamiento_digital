# Función sigmoide z’ = z - a * sin(2PI*z/A), donde a >0
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
import math
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io

image=io.imread("lena_gray.png")
# El rano de valores del pixel esta entre 0-255.

temp = np.copy(image)
largo = len(temp[0])
ancho = len(temp)

plt.title("Imagen original")
plt.imshow(image,vmin=0,vmax=255)
plt.show()
a = -1
A=255

while ((a < 0) or (a > 40)):
    a=float(input ("Valor de a: "))

#Cuenta los colores de la imagen
for i in range(0, largo):
    for j in range(0, ancho):
        color = temp[i,j]
        nuevo_color = A/2 * (1+math.tanh(a*(color-A/2)))

        temp[i,j]=nuevo_color

plt.title("Imagen Contraste funcion tangente hiperbolica senoidal")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()