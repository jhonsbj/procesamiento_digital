
import matplotlib.pyplot as plt
from skimage import io

img = io.imread("pubg.png")

print("Dimensiones de la imagen:")
plt.imshow(img)
plt.show()
ancho = len(img[0])
largo = len(img)
histograma = []
histograma_red = []
histograma_green = []
histograma_blue = []


for i in range(ancho):
    for j in range(largo):
        histograma.append(img[i,j,0])
        histograma.append(img[i,j,1])
        histograma.append(img[i,j,2])
        histograma_red.append(img[i,j,0])
        histograma_green.append(img[i,j,1])    
        histograma_blue.append(img[i,j,2])

plt.hist(histograma, 5, facecolor='red')
plt.ylabel('Frequencia')
plt.xlabel('Valores')
plt.title('Histograma')
plt.show()

plt.hist(histograma, 4, facecolor='blue')
plt.ylabel('Frequencia')
plt.xlabel('Valores')
plt.title('Histograma')
plt.show()

plt.hist(histograma, 3, facecolor='green')
plt.ylabel('Frequencia')
plt.xlabel('Valores')
plt.title('Histograma')
plt.show()