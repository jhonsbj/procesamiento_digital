# Ecualizacion del Histograma
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

histograma=[]
f=[]
acumulado = 0
np1 = largo*ancho
imagen_equalizada = []

#Inicializa el arreglo del histograma
for i in range(0,256):
    histograma.append(0)
    f.append(0)

#Cuenta los colores de la imagen
for i in range(0, largo):
    for j in range(0, ancho):
        color = temp[i,j]
        histograma[color] = histograma[color]+1 #contando del numero apariciones del color

acumulado = histograma[0]

#Calcula el valor de f para equalizar los colores
f[0]=0
for i in range(1,254):
    f[i]=acumulado*255/np1
    acumulado=acumulado+histograma[i]
f[255]=255

#Genera la nueva imagen con los colores equalizados
for i in range(largo):
    linea = []

    for j in range(ancho):
        color = temp[i,j]
        linea.append(f[color])
    
    imagen_equalizada.append(linea)

plt.title("Imagen Equalizada")
plt.imshow(imagen_equalizada,vmin=0,vmax=255)
plt.show()