
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
from skimage import io


image=io.imread("lena.png")/255.0 # imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

print("- Dimensiones de la imagen:")
print(image.shape)

plt.title("Imagen original")
plt.imshow(image)
plt.show()

temp=np.copy(image) # creo una copia de la imagen para preservar la original

ancho = len(temp)
largo = len(temp[0])
nivel = 0.5

for i in range(ancho):
    for j in range(largo):
        temp[i,j,0] = temp[i,j,0] + nivel
        temp[i,j,1] = temp[i,j,1] + nivel
        temp[i,j,2] = temp[i,j,2] + nivel
    
plt.title("Imagen aclarada")
plt.imshow(temp)
plt.show()

