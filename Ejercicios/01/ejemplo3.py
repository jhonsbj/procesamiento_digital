
# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt

from skimage import io


image=io.imread("lena.png")/255.0 # imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

print("- Dimensiones de la imagen:")
print(image.shape)
plt.imshow(image)
plt.show()
