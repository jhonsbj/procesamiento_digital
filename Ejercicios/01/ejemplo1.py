

# importamos el modulo pyplot, y lo llamamos plt
import matplotlib.pyplot as plt

#configuracion necesaria de pyplot para ver las imagenes en escala de grises
plt.rcParams['image.cmap'] = 'gray'

#tambien importamos numpy ya que lo usamos para crear y manipular matrices
import numpy as np

#tamaño de las matrices a visualizar
size=(20,30)

# Una matriz de ceros. 
imagen_negra = np.zeros(size)

#visualizamos la matriz
#Se ve como una imagen negra, ya que todos los elementos (pixeles) tienen intensidad 0
# plt.imshow(imagen_negra,vmin=0,vmax=1)
# (es necesario indicar vmin y vmax para que pyplot sepa que el minimo es 0 y el maximo 1)
# (solo imagenes escala de grises)

#plt.show()



# IMAGEN BLANCA
# Una matriz de unos. 
imagen_blanca = np.ones(size)

#visualizamos la matriz
#Se ve como una imagen blanca, ya que todos los elementos (pixeles) tienen intensidad 1
plt.imshow(imagen_blanca,vmin=0,vmax=1)

#creamos otra figura para mostrar la imagen (sino el proximo imshow sobreescribe al anterior)
plt.figure()

# IMAGEN GRIS
# Una matriz con valor 0.5 en todos sus elementos 
imagen_gris = np.ones(size)*0.1

#visualizamos la matriz
#Se ve como una imagen gris, ya que todos los elementos (pixeles) tienen intensidad 0.5
plt.imshow(imagen_gris,vmin=0,vmax=1)

#plt.show()



# IMAGEN GRIS OSCURO
# Una matriz con valor 0.2 en todos sus elementos 
#imagen_gris_oscuro = np.ones(size)*0.2

#visualizamos la matriz
#Se ve como una imagen gris, ya que todos los elementos (pixeles) tienen intensidad 0.5
#plt.imshow(imagen_gris_oscuro,vmin=0,vmax=1)

#creamos otra figura para mostrar la imagen (sino el proximo imshow sobreescribe al anterior)
#plt.figure()

# IMAGEN ALEATORIA
# Una matriz con valor aleatorio
imagen_aleatoria = np.random.rand(size[0],size[1])

#visualizamos la matriz
#Se ve como una imagen gris, ya que todos los elementos (pixeles) tienen intensidad 0.5
plt.imshow(imagen_aleatoria,vmin=0,vmax=1)
plt.show()