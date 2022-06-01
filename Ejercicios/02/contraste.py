# Función alto contraste
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
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
a = int(input ("Valor de a: "))

#Cuenta los colores de la imagen
for i in range(0, largo):
    for j in range(0, ancho):
        nuevo_color = a
        color = temp[i,j]

        if (color < a):
            nuevo_color = 0
        
        if (color > a):
            nuevo_color = 255
        
        temp[i,j]=nuevo_color

plt.title("Imagen Binaria")
plt.imshow(temp,vmin=0,vmax=255)
plt.show()