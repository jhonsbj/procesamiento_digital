
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

from skimage import io
.0
image=io.imread("lena_gray.png")/255.0
temp = np.copy(image)
ancho = len(temp[0])
largo = len(temp)
nivel = float(input("Nivel "))

plt.imshow(image,vmin=0,vmax=1)
plt.title("Imagen original")
plt.show()

for i in range(largo):
    for j in range(ancho):
        temp[i,j]=temp[i,j]+nivel

plt.title("Imagen aclarada al " + str(nivel*100) + "%")
plt.imshow(temp,vmin=0,vmax=1)
plt.show()

temp = np.copy(image)
for i in range(largo):
    for j in range(ancho):
        temp[i,j]=temp[i,j]-nivel

plt.title("Imagen obscurecida al " + str(nivel*100) + "%")
plt.imshow(temp,vmin=0,vmax=1)
plt.show()

temp = np.copy(image)
for i in range(largo):
    for j in range(ancho):
        temp[i,j]=temp[i,j]*0.5

plt.title("Imagen intensificada al " + str(nivel*100) + "%")
plt.imshow(temp,vmin=0,vmax=1)
plt.show()

temp = np.copy(image)
for i in range(largo):
    for j in range(ancho):
        temp[i,j]=temp[i,j]/0.5

plt.title("Imagen reducida al " + str(nivel*100) + "%")
plt.imshow(temp,vmin=0,vmax=1)
plt.show()