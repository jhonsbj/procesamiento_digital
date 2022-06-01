
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt
import numpy as np
from skimage import io


image=io.imread("lena.png")/255.0 # imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

print("- Dimensiones de la imagen:")
print(image.shape)
lena_red=np.copy(image) # creo una copia de la imagen para preservar la original
lena_red[:,:,1]=256
lena_red[:,:,2]=0
plt.title("Lena_ canal rojo")
plt.imshow(lena_red)

plt.show()



lena_red_green=np.copy(image) # creo una copia de la imagen para preservar la original
lena_red_green[:,:,2]=1
plt.title("Lena_ sin canal azul")
plt.imshow(lena_red_green)

plt.show()